# Integration Testing

> Thursday 26th 2019 (Week 4)

MagicMock() for mocking our app database manager. Can check the right things are called.

```python
# Arrange
------
db = DatabaseManager()
dbMock = MagicMock(wraps=db)
--OR--
dbMock = MagicMock(wraps=DatabaseManager)
------
app = app.App(db)

# Act
app.exit()

# Assert
dbMock.saveDrinks.assert_called()
```

