# Proposal: Workflow

> This proposal flexible and may change during the development time as needed.

## Goals

1. As loseless transition possible.
2. Having Beta on live deployment with real time data piping to spin into live seamlessly.
3. Reduce unnecessary performance bottlenecks.
4. Robust maintainibility and documentation of the system for easier handoffs in future, transparency and better understanding of the whole system.

## Technical Milestones (High level)

|What|Priority|Reason|
|---|---|---|
|**Database**|1|The API/backend is designed around the database.|
|**Backend design**|2|The backend layer will do the heavy lifting of loading/processing the data instead of handling everything at the application level (previous workflow).|
|**DB Ingestion pipeline**|3| Piping the data from the old database to the new DB.|
|**Frontend**|4|Once we have the API design ready, we can design the frontend and incrementally connect with the API layer.|

## Proposed tech stack:

1. Database: PostgreSQL
    - Multiple read write.
    - Diverse plugins.
    - ACID compliant.

2. Backend: Python
    - FastAPI for fast routes.
    - SQLalchemy + Alembic, a robust ORM for python + db migration management.
    - FastAPI security for native auth system.

3. Frontend: Vue + Nuxt
    - Dynamic renderings.
    - fast and smaller bundle size than react.
    - robust state management.

## Required tools:

- Hosting server for Alpha and Beta launches. The devs will primarily work on the local network. Only verified changes will be pulled on the Alpha and Beta (deployed) versions.
- Claude code (100$ plan) for the coding agent.
- PostgreSQL deployment (this will be needed from the very beginning because every dev instances wwill require this for prods and tests.)
- Full access + support for the development servers.

## Notes:
Two versions will be maintained till ready for **Production**.
- **Alpha**: Exclusive to only dev-team.
  - Smaller teams for domain-specific knowledge must be incorporated and have sessions with the dev.
  - the deployments will be solely for testing purpose to dev and this small team of domain-specific knowledge.
- **Beta**: More inclusive than Alpha.
  - Will be deployed to a larger pool of people if not everyone.
  - Anyone can check this version and provide feedback. 
