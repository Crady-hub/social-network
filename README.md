# social-network

Регистрация пользователя:
POST
http://localhost:8000/auth/users/

Авторизация/создание токен:
POST
http://localhost:8000/auth/jwt/create

Обновление токена:
POST
http://localhost:8000/auth/jwt/refresh

Список/создание поста:
GET, POST
http://localhost:8000/api/v1/post

Создание/обновление лайка:
POST
http://localhost:8000/api/v1/post/like

Статистика лайков:
GET
http://localhost:8000/api/v1/post/like/statistics
