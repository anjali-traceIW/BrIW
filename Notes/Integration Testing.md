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

Patching is a more granular way of mocking, but for functions as opposed to classes. Like a tiny mock. Can patch when user input is called for, and return some fake input for your function.

```python
@mock.patch("src.db_connector.db_interaction_fcn")
def test_this(self, db_interaction_fcn):
  db_mock = Mock()
  db_interaction_fcn.return_value = db_mock
  expected = {...}
  
  actual = do_something_that_uses_db_interaction_fcn()
  
  self.assert_Equal(expected, actual)
```

## Side Effect vs Return Value

Return value set one value, returns every time it's called

Side effect set a list of values, returns 1st object in the list first time it's called, 2nd object second time it's called, etc.

```python
@unittest.mock.patch('builtings.input', return_value='') # input_mock
@unittest.mock.patch('builtings.print', return_value='')	# print_mock
def test(self, print_mock, input_mock):
  # Stuff
```

Parameters are dectorators in reverse order (closest to function definition is first param).