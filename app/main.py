from fastapi import FastAPI

from app.routers import employees, review_periods, reviews

app = FastAPI(
    title="Employee Performance Review Management System",
    version="1.0.0",
)

app.include_router(employees.router, prefix="/api")
app.include_router(review_periods.router, prefix="/api")
app.include_router(reviews.router, prefix="/api")
