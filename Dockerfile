ARG PYTHON_VERSION=3.14.1

FROM python:${PYTHON_VERSION}-slim-trixie AS builder
ARG APP_VERSION
WORKDIR /app

# Install uv
# Ref: https://docs.astral.sh/uv/guides/integration/docker/#installing-uv
COPY --from=ghcr.io/astral-sh/uv:0.9.15 /uv /uvx /bin/

# Compile bytecode
# Ref: https://docs.astral.sh/uv/guides/integration/docker/#compiling-bytecode
ENV UV_COMPILE_BYTECODE=1
# uv Cache
# Ref: https://docs.astral.sh/uv/guides/integration/docker/#caching
ENV UV_LINK_MODE=copy

# Install dependencies (production only)
# Ref: https://docs.astral.sh/uv/guides/integration/docker/#intermediate-layers
COPY ./pyproject.toml ./uv.lock ./README.md /app/
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev --no-install-project

# Copy application code and install project
COPY ./my_app /app/my_app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

# Production stage
FROM python:${PYTHON_VERSION}-slim-trixie AS production
ARG APP_VERSION
WORKDIR /app

# Copy only the virtual environment from builder
COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app/my_app /app/my_app

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"
ENV APP_VERSION=${APP_VERSION}
ENV PYTHONPATH=/app

CMD ["python", "-m", "my_app"]
