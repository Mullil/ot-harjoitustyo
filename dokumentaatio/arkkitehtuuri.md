```mermaid
classDiagram
    UI --> RegisterView
    UI --> StartingView
    UI --> LoginView
    UI --> IndexView
    UI --> CreateCourseView
    LoginView --> UserService
    RegisterView --> UserService
    IndexView --> CourseService
    CreateCourseView --> CourseService
    UserService --> User
    CourseService --> Course
```
