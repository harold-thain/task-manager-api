## 1. FastAPI basics - running API with a couple of routes (HTTP methods, request/response, project structure)

Why FastAPI and not Flask?
Both are valid, but FastAPI is the better learning choice here because it gives you automatic data validation (via Pydantic), auto-generated docs (you'll see your API in a browser instantly), and it's modern Python — used heavily in production. Flask is older and more manual.

Why a virtual environment? Think of it like a clean room for your project. Without it, every Python project on your machine shares the same packages, which causes version conflicts. When your terminal shows (venv) at the start of the line, you're inside it

Why uvicorn? FastAPI doesn't run itself — it needs a server. Uvicorn is a fast, lightweight one designed for modern Python.

What's happening here?

FastAPI() creates your app
@app.get("/") is a decorator — it tells FastAPI "when someone sends a GET request to /, run this function"
The function just returns a Python dict — FastAPI automatically converts it to JSON
{name} in the path is a path parameter — FastAPI reads the type hint (name: str) and validates it for you

## 2. Task CRUD - full create/read/update/delete for tasks (REST design, status codes, data validation)

What you want to doHTTP MethodRouteWhy that method?Create a taskPOST/tasksPOST = "here's new data, create something"Get all tasksGET/tasksGET = "give me data, change nothing"Get one taskGET/tasks/{id}Same idea, scoped to one itemUpdate a taskPUT/tasks/{id}PUT = "replace this item entirely"Delete a taskDELETE/tasks/{id}DELETE = "remove this item"

Why two separate models? TaskCreate is what the user sends in — no ID yet because the server assigns that. TaskResponse is what we send back — it includes the ID. Keeping these separate prevents accidentally exposing fields you don't want to, and is a pattern you'll use constantly.
Why Pydantic? FastAPI uses Pydantic under the hood. When a request comes in, Pydantic automatically validates it against your model — wrong types, missing required fields, bad dates — all caught and returned as clear error messages automatically.

## 3. MySQL + SQLAlchemySwap in-memory data for a real databaseORM, models, migrations, relationships

hey're not competing at all — they do completely different jobs and you'll actually use both in the same project. Here's the clearest way to think about it:
PydanticSQLAlchemyJobValidates & shapes data in PythonTalks to a databaseThinks about"Is this request valid? What shape is the response?""How do I store/fetch this in MySQL?"Lives atThe API boundary (request comes in, response goes out)The database layerAnalogyA bouncer checking you meet the entry requirementsA warehouse manager who stores and retrieves your stuff

So the flow is:

HTTP Request
     ↓
Pydantic validates the shape        ← "is this data correct?"
     ↓
SQLAlchemy reads/writes to MySQL    ← "store it / fetch it"
     ↓
Pydantic formats the response       ← "send back the right shape"
     ↓
HTTP Response

What is `BaseModel`?
```
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
```
You're saying "inherit everything Pydantic knows how to do" — which is quite a lot. By subclassing BaseModel your class automatically gets:

Validation — if title isn't a string, Pydantic rejects it with a clear error (the 422 you saw)
Type coercion — if something can be safely converted it will be, e.g. "2025-01-01" → a real date object
Serialisation — .model_dump() turns your object into a plain Python dict, .model_dump_json() gives you JSON
A helpful __repr__ — so printing the object gives you something readable

Without BaseModel you'd just have a normal Python class and you'd have to write all that validation yourself, manually, for every field. Pydantic gives you it for free by inheritance.
A quick illustration of what it's actually doing behind the scenes:

```
# Without Pydantic — you'd have to do all this yourself
def create_task(data: dict):
    if "title" not in data:
        raise ValueError("title is required")
    if not isinstance(data["title"], str):
        raise ValueError("title must be a string")
    if "due_date" in data:
        try:
            datetime.strptime(data["due_date"], "%Y-%m-%d")
        except ValueError:
            raise ValueError("due_date must be a valid date")
    # ...and so on for every field

# With Pydantic — all of the above, for free
class TaskCreate(BaseModel):
    title: str
    due_date: Optional[date] = None
```
That's the core bargain: you describe the shape of your data using Python type hints, and Pydantic handles the rest.

We need a database — in-memory storage disappears the moment the process stops. A database persists independently of your running server, which is fundamental to any real application.

SQLiteMySQLWhere it livesA single .db file in your projectA separate running serverSetupZero — it's built into PythonRequires installation/DockerGood forDevelopment, learning, small appsProduction, multiple users, scaleIn our codeOne line changesOne line changes
The beautiful thing is that because we're using SQLAlchemy as an abstraction layer, swapping SQLite for MySQL later is literally changing one line — the connection string. All the actual database code stays identical. That's one of the main reasons ORMs like SQLAlchemy exist.

What's a session? Think of it like a shopping basket at a supermarket checkout. You open a session, make changes (add items, update things, delete things), then either commit (pay and take the items) or rollback (abandon the basket). This gives you control and safety — nothing hits the database until you deliberately commit.

Why does this look different from the Pydantic models? SQLAlchemy models describe storage — columns, types, constraints, relationships. Pydantic schemas describe communication — what comes in over HTTP and what goes out. Same data, two different representations, two different jobs.

What's from_attributes = True? By default Pydantic only reads plain dicts. SQLAlchemy returns objects with attributes (like task.title). This setting tells Pydantic "also look at object attributes, not just dict keys" — without it, your responses would fail.

What's Depends(get_db)? This is FastAPI's dependency injection system. Instead of opening a database session manually inside every route, you declare "I need a db session" and FastAPI calls get_db() for you and passes the result in. It also ensures the session closes properly after the request. Clean, reusable, testable.

How do sessions and dependency injection work?

## 4. AuthenticationRegistration, login, JWT tokensPassword hashing, protecting routes

How authenication works for the API:
```
1. REGISTER:  User sends name, email, password
                    ↓
              We hash the password and store the user in DB
                    ↓
              Return success (never echo the password back)

2. LOGIN:     User sends email + password
                    ↓
              We find the user, check the hash matches
                    ↓
              We generate a JWT token and return it

3. PROTECTED: User sends a request WITH the token in the header
                    ↓
              We verify the token is valid and not expired
                    ↓
              We extract which user it is from the token
                    ↓
              We only return THEIR tasks
```

5. Polish & wrap-upError handling, README, final reviewCode quality, deliverables
