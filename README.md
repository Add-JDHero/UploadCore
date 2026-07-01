# UploadCore

**UploadCore** is a C++ microservice for file upload, storage and asynchronous processing.

The project is built as a backend infrastructure service: the kind of service that could be plugged into a larger application when that application needs to accept and manage files.

Examples:

* marketplace product images;
* messenger attachments;
* user documents;
* lab archives;
* build artifacts;
* media uploads.

The point is not to build another cloud drive.

The point is to build a serious backend component and use it as a playground for real engineering problems: HTTP, storage, PostgreSQL, background workers, retries, consistency, metrics and load testing.

Why this project exists

I want to grow as a backend engineer by building something that feels close to production infrastructure.

UploadCore is not just about “uploading a file”.

A proper file upload service has a lot of interesting problems:

* how to accept large files without wasting memory;
* how to store metadata separately from file content;
* how to recover from broken uploads;
* how to keep PostgreSQL and file storage consistent;
* how to process uploaded files in the background;
* how to retry failed tasks;
* how to measure latency under load;
* how to understand where the bottleneck is.

This project exists to meet those problems directly.

Current status

Project bootstrap.

No service code yet.

Planned stack

* C++20
* userver
* PostgreSQL
* local filesystem storage
* Docker Compose
* later: background workers, task queue, metrics, load generator

First goal

The first goal is intentionally small:

```Plain text
Upload a file.
Store its metadata in PostgreSQL.
Store its content on disk.
Download it back by file id.
```

First planned API shape:

```Plain text
GET    /ping
POST   /v1/files/metadata
GET    /v1/files/{file_id}
PUT    /v1/files/{file_id}/content
GET    /v1/files/{file_id}/content
DELETE /v1/files/{file_id}
```

The first useful version should prove this flow:

```Plain text
client
  -> UploadCore HTTP API
  -> PostgreSQL metadata
  -> local file storage
  -> download by file_id
```

What UploadCore is not

UploadCore is not production-ready.

UploadCore is not a full S3 replacement.

UploadCore is not a frontend project.

UploadCore is a production-shaped learning project: small enough to build alone, but serious enough to contain real backend problems.

Future direction

After the basic upload/download flow works, the project will evolve step by step:

* file statuses;
* background processing;
* SHA-256 calculation;
* PostgreSQL-backed task queue;
* retries and dead tasks;
* cleanup of abandoned uploads;
* deduplication;
* load testing;
* latency measurements;
* metrics and observability.
