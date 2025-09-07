# Technology choices

## API: REST vs. gRPC
*   REST - JSON + HTTP/1.1
    + Native support in web browsers
    + Standard CRUD operations
    + Cacheable, stateless
    + Good for static data
    - Requires a new TCP handshake for each request
*   gRPC - Protocol Buffers + HTTP/2.1
    + Binary serialization creates smaller message sizes = faster transmission
    + Allows developers to use a combination of languages (e.g., protos can be packed by Typescript/Android/iOS clients)
    + Beneficial for applications requiring low latency + high throughput (mobile apps)
    + Good support for streaming patterns (like Chat applications)
    + Good for moving and updated data
    - Not many browsers are compatible with the required protocol

## App Server: Django vs. Node.js
*   Django - Python data + scientific libraries 
*   Node.js - Single Page Applications, real-time applications (like Chat applications)
    + Easy horizontal scaling

## Host: AWS vs. GCP
*   AWS - Great fault tolerance + high level of physical separation

## Deployment: ECS 
*   Containerized system - consistent hosting strategy for FE+BE
*   Easy scalibility
*   Keep services within Amazon VPC - security & control

## Cache: Redis
*   Distributed

## Database: PostgreSQL
*   Relational

## Object/image storage: S3

## Message queues: AWS Simple Queue Service (SQS) vs. Azure Queue Storage & Azure Service Bus vs. GCP – Cloud Pub/Sub
