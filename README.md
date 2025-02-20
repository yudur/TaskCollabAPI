# 🚀 Project Challenge: Collaborative API with FastAPI and Prisma

## **Objective**

Develop a **RESTful API** for task collaboration management using **FastAPI** and **Prisma ORM**. The system should allow users to create and manage tasks, collaborate with each other, and comment on activities.

## **Project Requirements**

✅ **User Authentication and Management**

- Create user accounts
- Login and authentication via JWT
- List registered users

✅ **Task Management**

- Create, edit, and delete tasks
- Assign tasks to specific users
- Mark tasks as completed

✅ **Comments and Interactions**

- Allow users to comment on tasks
- List all comments related to a task

✅ **Notifications and Updates** (Optional)

- Implement WebSockets for real-time notifications

✅ **Database**

- Use **Prisma ORM** connected to **PostgreSQL** or **SQLite**

## **Business Rules**

1. Only the task creator can edit or delete it
2. Only authenticated users can create and comment on tasks
3. Each task can be assigned to only one user

## **Suggested Technologies**

- **FastAPI** (Backend)
- **Prisma ORM** (Database)
- **JWT** (Authentication)
- **Pydantic** (Data validation)
- **Docker** (Optional)

## **Deliverables**

- Source code in a Git repository
- API documentation (Swagger/OpenAPI)
- `README.md` file with usage instructions

---

💡 **Bonus Challenge**: Implement a **permissions system** for different user roles (admin, collaborator, visitor).

🔹 **Difficulty**: ⭐⭐⭐⭐☆  
🔹 **Estimated Duration**: 5 to 7 days

Who accepts the challenge? 🚀🔥
