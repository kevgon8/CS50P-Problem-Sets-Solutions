from jar import Jar

def test_init():
    jar1 = Jar()
    assert jar1.capacity == 12 # @property method called
    jar2 = Jar(10)
    assert jar2.capacity == 10 # @property method called

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(5)
    assert jar.size == 6

def test_withdraw():
    jar = Jar()
    jar.deposit(9)
    jar.withdraw(6)
    assert jar.size == 3
    jar.withdraw(3)
    assert jar.size == 0
