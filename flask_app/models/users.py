from flask_app.config.mysqlconnection import connectToMySQL

class User:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM users'
        users_from_db = connectToMySQL('first_flask').query_db(query)
        users = []
        for i in users_from_db:
            users.append(cls(i))
        return users

    @classmethod
    def addUser(cls, data):
        query = 'INSERT INTO first_flask.users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);'
        user_id = connectToMySQL('first_flask').query_db(query, data)
        return user_id

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM first_flask.users WHERE id = %(id)s;'
        result = connectToMySQL('first_flask').query_db(query, data)
        return cls(result[0])

    @classmethod
    def updateUser(cls, data):
        query = "UPDATE users SET first_name= %(first_name)s, last_name= %(last_name)s, email= %(email)s,updated_at= NOW() WHERE id=%(id)s;"
        return connectToMySQL('first_flask').query_db(query, data)

    @classmethod
    def remove(cls,data):
        query = "DELETE FROM users WHERE id=%(id)s;"
        return connectToMySQL('first_flask').query_db(query,data)