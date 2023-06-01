# Szegedfoglalo
Szegedfoglalo is a captivating two-player online quiz game that immerses you in the fascinating world of Szeged, a vibrant city with a rich cultural heritage. In this game, you and your opponent engage in a thrilling battle to conquer territories and gather valuable points by answering questions about Szeged. Prepare yourself for an exhilarating gameplay experience as you explore the city's landmarks, history, and more.

## Note
This repository is only one of the five part of the whole project, it will not work alone.
However, you can try the game out at [Szegedfoglalo's homepage](http://szegedfoglalo.ddns.net/) if the hosting is still up.

# Technical Details
## Workflow
The development of Szegedfoglalo followed a well-structured workflow that integrated various tools and platforms:

- **Version Control**: We utilized GitLab as our version control system, allowing seamless collaboration and easy tracking of code changes.
- **Scrum Management**: ScrumMate was the chosen tool for agile project management. It facilitated efficient task management, sprint planning, and progress tracking throughout the development process.
- **Communication**: Discord served as our primary communication platform, enabling real-time discussions, information sharing, and team coordination.

## Backend
The backend of Szegedfoglalo was implemented using the Python programming language. Leveraging the flexibility and versatility of Python, we crafted a robust backend system to handle various game functionalities.

- **Framework**: The backend was developed using Flask, a popular and lightweight web framework in Python. Flask provided a solid foundation for building the game's API endpoints and handling HTTP requests.

## Database
To store and manage game-related data, we employed both MySQL and SQLite databases, each serving specific purposes:

- **MySQL**: We utilized MySQL to handle persistent data storage, such as user profiles, game progress, and leaderboard information. MySQL ensured efficient and reliable data retrieval and storage operations.
- **SQLite**: SQLite was employed for temporary storage, caching purposes, and for managing the game lobbies.

## Frontend
The frontend of Szegedfoglalo was crafted using a combination of web technologies to create an intuitive and visually appealing user interface:

- **HTML**
- **CSS**
- **JavaScript**: Dominant part of the game logic, and the connection with the Python codes.

## Other Technologies Used
In addition to the core technologies mentioned above, we incorporated various other tools and technologies to enhance the functionality and performance of Szegedfoglalo:

- **Websockets and Socket.IO**: We utilized websockets and Socket.IO to enable real-time bidirectional communication between the server and clients. This allowed for instantaneous updates, notifications, and multiplayer interactions within the game.
- **MVC Model**: The game's backend followed the Model-View-Controller (MVC) architectural pattern. This design pattern ensured a clear separation of concerns, making the codebase more organized, maintainable, and scalable. (We mostly used MVC model in a different repository of the project)
- **Uvicorn and FastAPI**: Uvicorn, in conjunction with the FastAPI framework, powered the backend server, providing high-performance and asynchronous capabilities. This allowed the game to handle a large number of concurrent requests efficiently.
These technologies and frameworks were meticulously selected and integrated to create a seamless and engaging gaming experience in Szegedfoglalo.

# The project
## Features
- **Territory Reservation**: Begin the game by strategically reserving territories on the map. Each territory represents a different location or aspect of Szeged, and your goal is to claim as many territories as possible to gain an advantage.

- **Quiz Challenges**: Test your knowledge about Szeged through a series of challenging quiz questions. Answer correctly to secure your hold on territories and earn valuable points. Be prepared to delve into the city's diverse topics, ranging from historical events to famous landmarks.

- **University Faculty Wars**: Once the reservation phase concludes, engage in intense battles with your opponent to occupy five prestigious university faculties. These faculties are the ultimate prize, granting you additional points and increasing your chances of victory. Prepare for a thrilling clash between the esteemed Faculty of Natural Sciences and the prestigious Faculty of Humanities.

## My work
- **Group Collaboration**: Szegedfoglalo was developed as part of an Agile Software Engineering course by a passionate group of 25 individuals. Over the course of four to five months, we worked tirelessly in five teams, each assigned to a different project. At the culmination of our efforts, we seamlessly merged all five projects to create this extraordinary game, providing you with an expansive and immersive gaming experience.

- **Scrum Master and Backend Developer**: As the Scrum Master and backend developer for this project, I meticulously orchestrated the development process and ensured the smooth integration of various components. I also developed game logic and map rules in Python and JavaScript.

## Acknowledgements
I would like to express my gratitude to our mentors of the Agile Software Engineering course and our fellow teammates for their dedication and hard work in bringing Szegedfoglalo to life. Special thanks to the Faculty of Natural Sciences and the Faculty of Humanities for providing the inspiration behind the eternal war in this game.

# Screenshots of pages
## Login
![login](login.png)

## Menu / Game Rules / Profile / Start Game
![lobby](lobby.gif)

## Lobby with chat
![chat](chat.gif)

## Gameplay
![gameplay](gameplay.gif)

## Result
![result](result.png)

