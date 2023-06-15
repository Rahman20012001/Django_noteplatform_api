﻿# django-noteplatform-api
 This repository contains the code for a note storage platform. The platform allows users to store textual, audio, and video notes. It also supports note sharing among users.

## Technologies Used

- Django
- Django REST Framework
- SQLite 

## Setup Instructions

1. Clone the repository.
2. Install the required dependencies.
3. Configure the database settings.
4. Run database migrations.
5. Start the development server.

## API Endpoints

- `/api/notes/` (GET, POST): Endpoint to list all notes or create a new note.
- `/api/notes/<note_id>/` (GET, PUT, DELETE): Endpoint to retrieve, update, or delete a specific note.
- `/api/users/` (GET, POST): Endpoint to list all users or create a new user.
- `/api/users/<user_id>/` (GET, PUT, DELETE): Endpoint to retrieve, update, or delete a specific user.

## Contribution Guidelines

Contributions are welcome! If you find any issues or want to enhance the platform, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature/fix.
3. Make the necessary changes.
4. Test your changes thoroughly.
5. Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
