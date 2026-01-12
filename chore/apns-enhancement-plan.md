# APNs Enhancement Plan

## Current State
- Token-based authentication implemented with JWT and ES256.
- Basic alert payload builder that supports title, subtitle, body, sound, and badge.
- Simple sync HTTP/2 client that sends a single device token or a list of tokens with limited header configuration.

## Objectives
- Provide a complete APNs client covering supported push types, headers, payload fields, delivery options, and environments.
- Offer ergonomic, typed builders for headers and payloads while retaining low-level control when needed.
- Support both synchronous and asynchronous sending with connection reuse, retries, and idempotency.
- Deliver clear error handling, observability hooks, and test coverage without embedding secrets or comments.

## Feature Backlog
### Authentication and Session Management
- Cache and refresh JWTs before expiry; allow key rotation and multiple signing keys.
- Optional provider certificate support for legacy flows if needed by adopters.
- Connection reuse with pooled HTTP/2 clients for sync and async modes; configurable timeouts and proxies.

### Request Headers
- Full header coverage: apns-push-type, apns-id, apns-expiration, apns-priority, apns-topic, apns-collapse-id, apns-time-sensitive (where applicable), apns-relevance-score, and apns-push-type variants per target.
- Validate header combinations per push type (for example, background requires priority 5).
- Utilities for deterministic apns-id generation to enable idempotent retries.

### Payload Composition
- Complete aps dictionary support: alert dictionary (including launch-image and localization keys), badge, sound (critical alert fields), content-available, mutable-content, category, thread-id, target-content-id, interruption-level, relevance-score, stale-date, filter-criteria, and event-timestamp where applicable.
- Support live activity updates (including event timestamps and stale dates) and communication notifications.
- Allow custom data outside aps while enforcing payload size constraints and UTF-8 validity.
- Builders for background, VoIP, file provider, complication, location, mdm, and push-to-talk payload shapes.

### Sending APIs
- High-level client methods for common cases (alert, background, live activity update) and a low-level send interface for custom payloads.
- Batch sending with bounded concurrency and retry strategy for transient errors (5xx, 429, idle connection resets).
- Async counterparts for all send methods using httpx.AsyncClient.
- Environment selection (production vs sandbox) per request or client.

### Error Handling and Observability
- Map APNs error reasons to typed exceptions with actionable messages.
- Structured logging hooks and optional metrics callbacks for success/failure, latency, and retry counts.
- Capture and expose apns-id for tracing; surface response headers for callers.

### Validation and Safety
- Preflight validation for payload size, required headers, push type constraints, and sound file naming rules.
- Input sanitization to avoid invalid JSON and to protect against injection of malformed headers.

### Documentation and Examples
- English README with quickstart, advanced usage, and troubleshooting.
- Examples covering alert, background, live activity, VoIP, and batch sending with retries.
- Versioning and change log to track API stability.

## Architecture Plan
- **auth**: JWT generation and caching, key rotation, optional certificate support.
- **headers**: Immutable header builder with validation per push type and utilities for idempotency.
- **payload**: Typed payload builders for aps and custom data with validators.
- **client**: Sync and async clients that manage httpx session lifecycle, retries, and batching.
- **errors**: Typed exceptions and reason mapping.
- **types**: Enums for push types, interruption levels, categories, and common constants.
- **config**: Settings object for timeouts, proxies, retries, environment selection, and telemetry hooks.

## Testing Strategy
- Unit tests for header and payload builders, including validation and size limits.
- Mocked HTTP tests for client request composition, retries, and error handling using httpx test utilities.
- Integration harness stubbed with configurable endpoints to simulate APNs responses.
- Static checks for packaging metadata and minimal linting where available.

## Delivery Roadmap
- **Milestone 1**: Restructure modules (auth, headers, payload, client, errors, types, config); add validation and typed builders for headers and payloads; maintain backward-compatible helpers.
- **Milestone 2**: Implement sync and async clients with retries, batching, apns-id generation, and environment overrides; expand tests.
- **Milestone 3**: Add specialized payload support (live activities, background, VoIP, file provider, mdm), observability hooks, and documentation overhaul.
- **Milestone 4**: Finalize examples, changelog, and release automation; prepare for semantic versioned release.
