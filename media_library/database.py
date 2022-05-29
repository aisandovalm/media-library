# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


def _createMoviesTable():
    """Create the movies table in the database."""
    createTableQuery = QSqlQuery()
    return createTableQuery.exec(
        """
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            title VARCHAR(40) NOT NULL,
            year INTEGER,
            genre VARCHAR(40),
            director VARCHAR(40),
            writer VARCHAR(40)
        )
        """
    )


def _createGamesTable():
    """Create the games table in the database."""
    createTableQuery = QSqlQuery()
    return createTableQuery.exec(
        """
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            title VARCHAR(40) NOT NULL,
            year INTEGER,
            genre VARCHAR(40),
            creator VARCHAR(40),
            studio VARCHAR(40)
        )
        """
    )


def _createMusicTable():
    """Create the music table in the database."""
    createTableQuery = QSqlQuery()
    return createTableQuery.exec(
        """
        CREATE TABLE IF NOT EXISTS music (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            title VARCHAR(40) NOT NULL,
            artist VARCHAR(40) NOT NULL,
            album VARCHAR(40),
            year INTEGER,
            genre VARCHAR(40)
        )
        """
    )


def createConnection(databaseName):
    """Create and open a database connection."""
    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(databaseName)

    if not connection.open():
        QMessageBox.warning(
            None,
            "Media Library",
            f"Database Error: {connection.lastError().text()}",
        )
        return False

    _createMoviesTable()
    _createGamesTable()
    _createMusicTable()
    return True
