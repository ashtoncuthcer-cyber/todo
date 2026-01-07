# 📝 To-Do List Application

> *A modern, full-stack to-do list management system with FastAPI backend and React frontend*

---

## 🎯 Overview

This is a production-ready to-do list application that enables users to organize, manage, and track their tasks efficiently. Built with cutting-edge technologies, it provides a seamless experience across web platforms.

### **Tech Stack**

| Component | Technology | Version |
|-----------|-----------|---------|
| **Frontend** | React.js | Latest |
| **Backend** | FastAPI | Latest |
| **Database** | MongoDB | Latest |
| **Web Server** | Nginx | Latest |
| **Containerization** | Docker & Docker Compose | Latest |

---

## 🚀 Getting Started

### Prerequisites
- Docker and Docker Compose installed
- MongoDB instance running (configured via `MONGODB_URI`)

### Installation & Deployment

```bash
# Clone the repository
git clone <repository-url>
cd todo

# Start all services with Docker Compose
docker-compose -f compose.yml up -d

# Access the application
# Frontend: http://localhost (via Nginx)
# Backend API: http://localhost:3001
```

---

# 📡 Backend API Documentation

## **Base URL**
```
http://localhost:3001/api
```

---

## 📋 **List Management Endpoints**

### 1️⃣ **Get All To-Do Lists**

Retrieve a summary of all to-do lists with item counts.

```http
GET /api/lists
```

#### **Response** `200 OK`

```json
[
  {
    "id": "507f1f77bcf86cd799439011",
    "name": "Shopping",
    "item_count": 5
  },
  {
    "id": "507f1f77bcf86cd799439012",
    "name": "Work Projects",
    "item_count": 3
  }
]
```

---

### 2️⃣ **Create a New To-Do List**

Create a new to-do list with a specified name.

```http
POST /api/lists
Content-Type: application/json
```

#### **Request Body**

```json
{
  "name": "Grocery List"
}
```

#### **Response** `201 Created`

```json
{
  "id": "507f1f77bcf86cd799439013",
  "name": "Grocery List"
}
```

---

### 3️⃣ **Get a Specific To-Do List**

Retrieve a single to-do list with all its items.

```http
GET /api/lists/{list_id}
```

#### **Path Parameters**

| Parameter | Type | Description |
|-----------|------|-------------|
| `list_id` | string | MongoDB ObjectId of the list |

#### **Response** `200 OK`

```json
{
  "id": "507f1f77bcf86cd799439011",
  "name": "Shopping",
  "items": [
    {
      "id": "a1b2c3d4e5f6g7h8",
      "label": "Milk",
      "checked": false
    },
    {
      "id": "i9j0k1l2m3n4o5p6",
      "label": "Eggs",
      "checked": true
    }
  ]
}
```

---

### 4️⃣ **Delete a To-Do List**

Delete an entire to-do list and all its items.

```http
DELETE /api/lists/{list_id}
```

#### **Path Parameters**

| Parameter | Type | Description |
|-----------|------|-------------|
| `list_id` | string | MongoDB ObjectId of the list |

#### **Response** `200 OK`

```json
true
```

---

## 📌 **Item Management Endpoints**

### 5️⃣ **Create a New Item in a List**

Add a new to-do item to an existing list.

```http
POST /api/lists/{list_id}/items/
Content-Type: application/json
```

#### **Path Parameters**

| Parameter | Type | Description |
|-----------|------|-------------|
| `list_id` | string | MongoDB ObjectId of the list |

#### **Request Body**

```json
{
  "label": "Buy tomatoes"
}
```

#### **Response** `201 Created`

```json
{
  "id": "507f1f77bcf86cd799439011",
  "name": "Shopping",
  "items": [
    {
      "id": "t7u8v9w0x1y2z3a4",
      "label": "Buy tomatoes",
      "checked": false
    }
  ]
}
```

---

### 6️⃣ **Delete an Item from a List**

Remove a specific item from a to-do list.

```http
DELETE /api/lists/{list_id}/items/{item_id}
```

#### **Path Parameters**

| Parameter | Type | Description |
|-----------|------|-------------|
| `list_id` | string | MongoDB ObjectId of the list |
| `item_id` | string | Unique identifier of the item |

#### **Response** `200 OK`

```json
{
  "id": "507f1f77bcf86cd799439011",
  "name": "Shopping",
  "items": [
    {
      "id": "i9j0k1l2m3n4o5p6",
      "label": "Eggs",
      "checked": true
    }
  ]
}
```

---

### 7️⃣ **Update Item Checked State**

Toggle the completion status of a to-do item.

```http
PATCH /api/lists/{list_id}/checked_state
Content-Type: application/json
```

#### **Path Parameters**

| Parameter | Type | Description |
|-----------|------|-------------|
| `list_id` | string | MongoDB ObjectId of the list |

#### **Request Body**

```json
{
  "item_id": "a1b2c3d4e5f6g7h8",
  "checked_state": true
}
```

#### **Response** `200 OK`

```json
{
  "id": "507f1f77bcf86cd799439011",
  "name": "Shopping",
  "items": [
    {
      "id": "a1b2c3d4e5f6g7h8",
      "label": "Milk",
      "checked": true
    },
    {
      "id": "i9j0k1l2m3n4o5p6",
      "label": "Eggs",
      "checked": true
    }
  ]
}
```

---

## 🧪 **Utility Endpoints**

### 8️⃣ **Get Dummy Response** *(Testing/Health Check)*

A test endpoint that returns a dummy response with timestamp.

```http
GET /api/dummy
```

#### **Response** `200 OK`

```json
{
  "id": "507f191e810c19729de860ea",
  "when": "2026-01-07T14:32:15.123456"
}
```

---

## 📊 **Data Models**

### ***ListSummary* Model**

Lightweight representation of a to-do list.

```json
{
  "id": "string (MongoDB ObjectId)",
  "name": "string",
  "item_count": "integer"
}
```

### ***ToDoList* Model**

Complete representation of a to-do list with items.

```json
{
  "id": "string (MongoDB ObjectId)",
  "name": "string",
  "items": [
    {
      "id": "string (UUID hex)",
      "label": "string",
      "checked": "boolean"
    }
  ]
}
```

### ***ToDoListItem* Model**

Individual to-do list item.

```json
{
  "id": "string (UUID hex)",
  "label": "string",
  "checked": "boolean"
}
```

---

## ⚙️ **Configuration**

### Environment Variables

Configure the backend using the following environment variables:

| Variable | Description | Example |
|----------|-------------|---------|
| `MONGODB_URI` | MongoDB connection string | `mongodb+srv://user:pass@cluster.mongodb.net/?retryWrites=true` |
| `MONGODB_DB` | Database name (fallback if not in URI) | `todo_db` |
| `DEBUG` | Enable debug mode | `true`, `false` |

### Docker Compose Setup

The `compose.yml` orchestrates the entire application:

- **Frontend**: React application served via Nginx on port 80
- **Backend**: FastAPI server on port 3001
- **MongoDB**: Database service for data persistence
- **Nginx**: Reverse proxy and static file server

---

## 🔄 **API Usage Flow**

```
┌─────────────┐
│   Frontend  │
│  (React.js) │
└──────┬──────┘
       │
       │ HTTP Requests
       ↓
┌─────────────────┐
│ Nginx (Reverse) │
│     Proxy       │
└────────┬────────┘
         │
    ┌────┴────┐
    ↓         ↓
┌────────┐ ┌──────────────┐
│Backend │ │  Static      │
│(FastAPI)│ │  Files       │
└────┬───┘ └──────────────┘
     │
     ↓
 ┌────────────┐
 │  MongoDB   │
 │ Database   │
 └────────────┘
```

---

## 🛡️ **Error Handling**

The API returns standard HTTP status codes:

| Status Code | Meaning |
|-------------|---------|
| **200** | OK - Request successful |
| **201** | Created - Resource successfully created |
| **400** | Bad Request - Invalid input |
| **404** | Not Found - Resource doesn't exist |
| **500** | Internal Server Error - Server error |

---

## 📝 **Example Usage with cURL**

### Get all lists
```bash
curl -X GET http://localhost:3001/api/lists
```

### Create a new list
```bash
curl -X POST http://localhost:3001/api/lists \
  -H "Content-Type: application/json" \
  -d '{"name": "Work Tasks"}'
```

### Add an item to a list
```bash
curl -X POST http://localhost:3001/api/lists/{list_id}/items/ \
  -H "Content-Type: application/json" \
  -d '{"label": "Complete project"}'
```

### Mark an item as completed
```bash
curl -X PATCH http://localhost:3001/api/lists/{list_id}/checked_state \
  -H "Content-Type: application/json" \
  -d '{"item_id": "item_uuid", "checked_state": true}'
```

### Delete a list
```bash
curl -X DELETE http://localhost:3001/api/lists/{list_id}
```

---

## 🎨 **Frontend Features**

- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Real-time Updates**: Instant feedback for all operations
- **Intuitive UI**: Clean and user-friendly interface
- **Item Management**: Add, delete, and mark items as complete
- **List Organization**: Create and manage multiple to-do lists

---

## 📦 **Project Structure**

```
todo/
├── backend/
│   ├── src/
│   │   ├── server.py          # FastAPI application & routes
│   │   ├── dal.py             # Data Access Layer
│   │   └── __pycache__/
│   ├── Dockerfile
│   ├── pyproject.toml
│   └── requirements.txt
├── frontend/
│   ├── public/
│   │   ├── index.html
│   │   ├── manifest.json
│   │   └── robots.txt
│   ├── src/
│   │   ├── App.js             # Main React component
│   │   ├── App.css
│   │   ├── ListToDoLists.js   # Lists display component
│   │   ├── ToDoList.js        # Individual list component
│   │   └── index.js
│   ├── package.json
│   └── README.md
├── nginx/
│   └── nginx.conf             # Nginx configuration
├── compose.yml                # Docker Compose configuration
└── README.md                  # This file
```

---

## 🤝 **Contributing**

Contributions are welcome! Please follow the existing code style and submit pull requests for any improvements.

---

## 📄 **License**

This project is licensed under the MIT License.

---

## 💡 **Tips for Best Performance**

1. **Use list_id caching** in the frontend to reduce API calls
2. **Batch operations** when possible to minimize round trips
3. **Monitor MongoDB** connection pool for large deployments
4. **Enable Nginx caching** for static assets
5. **Use environment-specific configurations** for dev, staging, and production

---

<div align="center">

**Built with ❤️ for productivity**

*Last Updated: January 2026*

</div>
