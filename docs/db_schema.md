# Database Schema – Task Management System

## users
- id (PK)
- email (unique, not null)
- hashed_password
- name
- role_id (FK)
- role (relationship "Role" table)

## roles
- role-id (PK)
- role-name (unique)

## projects
- project-id (PK)
- project-name
- start_date
- end_date

## tasks master table - type
- id (PK)
- task-type 

## task status table
- id (PK)
- task-status(unique, not null)

## task priority table
- id (PK)
- task-priority(unique, not null)

## task table
- id (PK)
- task-title
- project-id → projects (FK)
- task-type-id → tasks master table (FK)
- task-status-id → task status table (FK)
- task-priority-id → task priority table (FK)

## user-task history
- id
- user_id
- task_id
- role_name

## project template
- id (PK)
- name
- description



## Relationships
- User → Projects (1:N)
- Project → Tasks (1:N)
- User → Tasks (1:N)
