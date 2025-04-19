from contextlib import closing
from django.db import connection

def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))


def get_gallery():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM lager_app_gallery""")
        galleries = dict_fetchall(cursor)
        return galleries


def get_education():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM lager_app_education""")
        educations = dict_fetchall(cursor)
        return educations


def get_activity():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM lager_app_activities""")
        activities = dict_fetchall(cursor)
        return activities


def get_rest_area():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM lager_app_restarea""")
        rest_areas = dict_fetchall(cursor)
        return rest_areas