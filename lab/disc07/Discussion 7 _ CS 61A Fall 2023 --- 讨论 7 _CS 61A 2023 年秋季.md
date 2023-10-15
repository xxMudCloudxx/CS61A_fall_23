> [Discussion 7 | CS 61A Fall 2023 --- 讨论 7 |CS 61A 2023 年秋季](https://cs61a.org/disc/disc07/#q4-that-s-inheritance-init)


You are currently logged in, so your work will be saved for you to re-visit later.

This discussion worksheet is for the Rao offering of CS 61A. Your work is not graded and you do not need to submit anything.  
此讨论工作表适用于 CS 61A 的 Rao 产品。您的作品没有评分，您不需要提交任何内容。

Consult the drop-down if you need a refresher on Object-Oriented Programming. It's okay to skip directly to the questions and refer back here should you get stuck.  
如果您需要复习面向对象编程，请参阅下拉列表。可以直接跳到问题，如果您遇到困难，可以在此处参考。  

**Object-oriented programming** (OOP) is a programming paradigm that allows us to treat data as objects, like we do in real life.  
面向对象编程（OOP）是一种编程范式，它允许我们将数据视为对象，就像我们在现实生活中所做的那样。

For example, consider the **class** `Student`. Each of you as individuals is an **instance** of this class.  
例如，考虑类 `Student` 。你们每个人都是这个类的一个实例。

Details that all CS 61A students have, such as `name`, are called **instance variables**. Every student has these variables, but their values differ from student to student. A variable that is shared among all instances of `Student` is known as a **class variable**. For example, the `extension_days` attribute is a class variable as it is a property of all students.  
所有 CS 61A 学生都有的详细信息（例如 `name` ）称为实例变量。每个学生都有这些变量，但它们的值因学生而异。在 `Student` 的所有实例之间共享的变量称为类变量。例如， `extension_days` 属性是一个类变量，因为它是所有学生的属性。

All students are able to do homework, attend lecture, and go to office hours. When functions belong to a specific object, they are called **methods**. In this case, these actions would be methods of `Student` objects.  
所有学生都可以做家庭作业、听讲座和上班时间。当函数属于特定对象时，它们称为方法。在这种情况下，这些操作将是 `Student` 对象的方法。

Here is a recap of what we discussed above:  
以下是我们上面讨论的内容的回顾：

*   **class**: a template for creating objects  
    类：用于创建对象的模板
*   **instance**: a single object created from a class  
    实例：从类创建的单个对象
*   **instance variable**: a data attribute of an object, specific to an instance  
    实例变量：特定于实例的对象的数据属性
*   **class variable**: a data attribute of an object, shared by all instances of a class  
    类变量：对象的数据属性，由类的所有实例共享
*   **method**: a bound function that may be called on all instances of a class  
    方法：可以在类的所有实例上调用的绑定函数

Instance variables, class variables, and methods are all considered **attributes** of an object.  
实例变量、类变量和方法都被视为对象的属性。

### Q1: WWPD: Legally Blonde OOP Q1：WWPD：合法的金发女郎 OOP

Below we have defined the classes `Student` and `Professor`. Remember that Python passes the `self` argument implicitly to methods when calling the method directly on an object.  
下面我们定义了类 `Student` 和 `Professor` 。请记住，Python 在直接在对象上调用方法时，会将 `self` 参数隐式传递给方法。

```
class Student:

    extension_days = 3 # this is a class variable

    def __init__(self, name, staff):
        self.name = name # this is an instance variable
        self.understanding = 0
        staff.add_student(self)
        print("Added", self.name)

    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)

class Professor:

    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def assist(self, student):
        student.understanding += 1

    def grant_more_extension_days(self, student, days):
        student.extension_days = days
```

What will the following lines output?  
以下行将输出什么？

```
>>> callahan = Professor("Callahan")
>>> elle = Student("Elle", callahan)
```

Saved at 1697366933676.

```
>>> elle.visit_office_hours(callahan)
```

Saved at 1697367004858.

```
>>> elle.visit_office_hours(Professor("Paulette"))
```

Saved at 1697367031134.

```
>>> elle.understanding
```

Saved at 1697367033780.

```
>>> [name for name in callahan.students]
```

Saved at 1697367127332.

```
>>> x = Student("Vivian", Professor("Stromwell")).name
```

Saved at 1697367133305.

```
>>> x
```

Saved at 1697367148441.

<pre><code>>>> [name for name in callahan.students]</code></pre> <label class="sr-only" for="oop-wwpd-8-input">Your Answer:</label> <input class="form-control storable" id="oop-wwpd-8-input" type="text"> <div class="storable-status"></div>

```
>>> elle.extension_days
```

Saved at 1697367154155.

```
>>> callahan.grant_more_extension_days(elle, 7)
>>> elle.extension_days
```

Saved at 1697367222766.

```
>>> Student.extension_days
```

Saved at 1697367165654.

### Q2: Email

We would like to write three different classes (`Server`, `Client`, and `Email`) to simulate a system for sending and receiving emails. A `Server` has a dictionary mapping client names to `Client` objects, and can both send `Email`s to `Client`s in the `Server` and register new `Client`s. A `Client` can both compose emails (which first creates a new `Email` object and then sends it to the recipient client through the server) and receive an email (which places an email into the client's inbox).  
我们想编写三个不同的类（ `Server` 、 `Client` 和 `Email` ）来模拟发送和接收电子邮件的系统。 `Server` 具有将客户端名称映射到 `Client` 对象的字典，并且可以将 `Email` s 发送到 `Server` 中的 `Client` s，并注册新的 `Client` s。 `Client` 既可以撰写电子邮件（首先创建新的 `Email` 对象，然后通过服务器将其发送到收件人客户端），也可以接收电子邮件（将电子邮件放入客户端的收件箱）。

Emails will only be sent/received within the same server, so clients will always use the server they're registered in to send emails to other clients that are registered in the same rerver.  
电子邮件将仅在同一服务器内发送 / 接收，因此客户端将始终使用它们注册的服务器向在同一服务器中注册的其他客户端发送电子邮件。

**An example flow:** A `Client` object (Client 1) composes an `Email` object with message `"hello"` with recipient Client 2, which the `Server` routes to Client 2's inbox.  
示例流： `Client` 对象（客户端 1）由一个 `Email` 对象组成，其中包含收件人客户端 2 的消息 `"hello"` ， `Server` 将其路由到客户端 2 的收件箱。

![](https://cs61a.org/disc/disc07/assets/email.png)

To solve this problem, we'll split the section into two halves (students on the left and students on the right): <ul> <li>Everyone will implement the <code>Email</code> class together</li> <li>The first half (left) will implement the <code>Server</code> class</li> <li>The other half (right) will implement the <code>Client</code> class

Fill in the definitions below to finish the implementation!  
填写下面的定义以完成实施！

Enter to Rename, Shift+Enter to Preview

Run in 61A Code 在 61A 代码中运行

Enter to Rename, Shift+Enter to Preview

Run in 61A Code 在 61A 代码中运行

Enter to Rename, Shift+Enter to Preview

Run in 61A Code 在 61A 代码中运行

### Q3: Keyboard

Below is the definition of a `Button` class, which represents a button on a keyboard. It has three attributes: `pos` (numerical position of the button on the keyboard), `key` (the letter of the button), and `times_pressed` (the number of times the button is pressed).  
下面是 `Button` 类的定义，它表示键盘上的按钮。它有三个属性： `pos` （键盘上按钮的数字位置）、 `key` （按钮的字母）和 `times_pressed` （按下按钮的次数）。

```
class Button:
    def __init__(self, pos, key):
        self.pos = pos
        self.key = key
        self.times_pressed = 0
```

We'd like to create a `Keyboard` class that takes in an arbitrary number of `Button`s and stores these `Button`s in a dictionary. The keys in the dictionary will be `int`s that represent the position on the `Keyboard`, and the values will be the respective `Button`. Fill out the methods in the `Keyboard` class according to each description.  
我们想创建一个 `Keyboard` 类，该类接收任意数量的 `Button` 并将这些 `Button` s 存储在字典中。字典中的键将是 `int` s，表示 `Keyboard` 上的位置，值将是相应的 `Button` 。根据每个说明填写 `Keyboard` 类中的方法。

**Important:** Utilize the doctests as a reference for the behavior of a `Keyboard` instance.  
重要提示：利用文档测试作为 `Keyboard` 实例行为的参考。

*   **Hint:** You can iterate over `*args` as if it were a list.  
    提示：您可以像循环访问列表一样循环访问 `*args` 。

Enter to Rename, Shift+Enter to Preview

Run in 61A Code 在 61A 代码中运行

Consult the drop-down if you need a refresher on Inheritance. It's okay to skip directly to the questions and refer back here should you get stuck.  
如果您需要复习继承，请参阅下拉列表。可以直接跳到问题，如果您遇到困难，可以在此处参考。  

To avoid redefining attributes and methods for similar classes, we can write a single **base class** from which the similar classes **inherit**. For example, we can write a class called `Pet` and define `Dog` as a **subclass** of `Pet`:  
为了避免重新定义类似类的属性和方法，我们可以编写一个类似的类继承的单个基类。例如，我们可以编写一个名为 `Pet` 的类，并将 `Dog` 定义为 `Pet` 的子类：

```
class Pet:

    def __init__(self, name, owner):
        self.is_alive = True    # It's alive!!!
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)

class Dog(Pet):

    def talk(self):
        super().talk()
        print('This Dog says woof!')
```

Inheritance represents a hierarchical relationship between two or more classes where one class **is a** more specific version of the other: a dog **is a** pet (We use **is a** to describe this sort of relationship in OOP languages, and not to refer to the Python `is` operator).  
继承表示两个或多个类之间的层次结构关系，其中一个类是另一个类的更具体版本：狗是宠物（我们使用 is 来描述 OOP 语言中的这种关系，而不是指 Python `is` 运算符）。

Since `Dog` inherits from `Pet`, the `Dog` class will also inherit the `Pet` class's methods, so we don't have to redefine `__init__` or `eat`. We do want each `Dog` to `talk` in a `Dog`-specific way, so we can **override** the `talk` method.  
由于 `Dog` 继承自 `Pet` ， `Dog` 类也会继承 `Pet` 类的方法，所以我们不必重新定义 `__init__` 或 `eat` 。我们确实希望每个 `Dog` 以 `Dog` 特定的方式 `talk` ，因此我们可以覆盖 `talk` 方法。

We can use `super()` to refer to the superclass of `self`, and access any superclass methods as if we were an instance of the superclass. For example, `super().talk()` in the `Dog` class will call the `talk()` method from the `Pet` class, but passing the `Dog` instance as the `self`.  
我们可以使用 `super()` 来引用 `self` 的超类，并访问任何超类方法，就好像我们是超类的实例一样。例如， `Dog` 类中的 `super().talk()` 将从 `Pet` 类调用 `talk()` 方法，但将 `Dog` 实例作为 `self` 传递。

This is a little bit of a simplification, and if you're interested you can read more in the [Python documentation](https://docs.python.org/3/library/functions.html#super) on `super`.  
这是一个简化，如果你有兴趣，你可以在 `super` 上的 Python 文档中阅读更多内容。

### Q4: That's inheritance, **init**? Q4：这就是继承，初始化？

Let's say we want to create a class `Monarch` that inherits from another class, `Butterfly`. We've partially written an `__init__` method for `Monarch`. For each of the following options, state whether it would correctly complete the method so that every instance of `Monarch` has all of the instance attributes of a `Butterfly` instance. You may assume that a monarch butterfly has the default value of 2 wings.  
假设我们要创建一个从另一个类 `Butterfly` 继承的类 `Monarch` 。我们已经为 `Monarch` 部分编写了一个 `__init__` 方法。对于以下每个选项，请说明它是否正确完成方法，以便 `Monarch` 的每个实例都具有 `Butterfly` 实例的所有实例属性。您可以假设帝王蝶的默认值为 2 个翅膀。

Enter to Rename, Shift+Enter to Preview

Run in 61A Code 在 61A 代码中运行

```
super.__init__()
```

Saved at 1697369314526.

```
super().__init__()
```

Saved at 1697369315966.

```
Butterfly.__init__()
```

Saved at 1697369315230.

```
Butterfly.__init__(self)
```

Saved at 1697369316710.

Some butterflies like the [Owl Butterfly](https://en.wikipedia.org/wiki/Owl_butterfly) have adaptations that allow them to mimic other animals with their wing patterns. Let's write a class for these `MimicButterflies`. In addition to all of the instance variables of a regular `Butterfly` instance, these should also have an instance variable `mimic_animal` describing the name of the animal they mimic. Fill in the blanks in the lines below to create this class.  
像猫头鹰蝴蝶这样的一些蝴蝶具有适应性，使它们能够用翅膀图案模仿其他动物。让我们为这些 `MimicButterflies` 编写一个类。除了常规 `Butterfly` 实例的所有实例变量外，这些实例还应该有一个实例变量 `mimic_animal` ，用于描述它们模仿的动物的名称。填写以下行中的空白以创建此类。

Enter to Rename, Shift+Enter to Preview

Run in 61A Code 在 61A 代码中运行

<pre><code>class MimicButterfly(Butterfly): def __init__(self, mimic_animal): super().__init__() self.mimic_animal = mimic_animal</code></pre> What expression completes the first blank? <label class="sr-only" for="butterfly-5-input">Your Answer:</label> <input class="form-control storable" id="butterfly-5-input" type="text"> <div class="storable-status"></div> <p>What expression completes the second blank? <label class="sr-only" for="butterfly-6-input">Your Answer:</label> <input class="form-control storable" id="butterfly-6-input" type="text"> <div class="storable-status"></div> </p> <p>What expression completes the third blank? <label class="sr-only" for="butterfly-7s-input">Your Answer:</label> <input class="form-control storable" id="butterfly-7s-input" type="text"> <div class="storable-status"></div>

### Q5: Cat

Below is the implementation of a `Pet` class. Each pet has three instance attributes (`is_alive`, `name`, and `owner`), as well as two class methods (`eat` and `talk`).  
下面是 `Pet` 类的实现。每个宠物有三个实例属性（ `is_alive` 、 `name` 和 `owner` ），以及两个类方法（ `eat` 和 `talk` ）。

```
class Pet():

    def __init__(self, name, owner):
        self.is_alive = True    # It's alive!!!
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)
```

Below is a skeleton for the <code>Cat</code> class, which inherits from the <code>Pet</code> class we saw in the Inheritance introduction. To complete the implementation, override the <code>__init__</code> and <code>talk</code> methods and add a new <code>lose_life</code> method.

Implement the `Cat` class, which inherits from the `Pet` class seen above. To complete the implementation, override the `__init__` and `talk` methods and add a new `lose_life` method.  
实现 `Cat` 类，该类继承自上面看到的 `Pet` 类。若要完成实现，请重写 `__init__` 和 `talk` 方法，并添加新的 `lose_life` 方法。

Hint: You can call the `__init__` method of `Pet` (the superclass of `Cat`) to set a cat's `name` and `owner`.  
提示：可以调用 `Pet` 的 `__init__` 方法（ `Cat` 的超类）来设置猫的 `name` 和 `owner` 。

Hint: The `__init__` method can be called at any point and used just like any other method.  
提示： `__init__` 方法可以随时调用，并像任何其他方法一样使用。

Enter to Rename, Shift+Enter to Preview

Run in 61A Code 在 61A 代码中运行

### Q6: NoisyCat

More cats! Fill in this implementation of a class called `NoisyCat`, which is just like a normal `Cat`. However, `NoisyCat` talks a lot: in fact, it talks twice as much as a regular `Cat`! If you'd like to test your code, feel free to copy over your solution to the `Cat` class above.  
更多的猫！填写一个名为 `NoisyCat` 的类的实现，它就像普通的 `Cat` 一样。然而， `NoisyCat` 说了很多：事实上，它说话的次数是普通 `Cat` 的两倍！如果要测试代码，请随时将解决方案复制到上面的 `Cat` 类。

Enter to Rename, Shift+Enter to Preview

Run in 61A Code 在 61A 代码中运行

Consult the drop-down if you need a refresher on `repr` and `str`. It's okay to skip directly to the questions and refer back here should you get stuck.  
如果您需要复习 `repr` 和 `str` ，请参阅下拉列表。可以直接跳到问题，如果您遇到困难，可以在此处参考。  

There are two main ways to produce the "string" of an object in Python: `str()` and `repr()`. While the two are similar, they are used for different purposes.

`str()` is used to describe the object to the end user in a "Human-readable" form, while `repr()` can be thought of as a "Computer-readable" form mainly used for debugging and development.

When we define a class in Python, `__str__` and `__repr__` are both built-in methods for the class.

We can call those methods using the global built-in functions `str(obj)` or `repr(obj)` instead of dot notation, `obj.__repr__()` or `obj.__str__()`.

In addition, the `print()` function calls the `__str__` method of the object and displays the returned string **with the quotations removed**, while simply calling the object in interactive mode in the interpreter calls the `_repr__` method and displays the returned string **with the quotations removed**.

Here are some examples:

```
class Rational:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)

    def __repr__(self):
        return 'Rational' + '(' + str(self.numerator) + ',' + str(self.denominator) + ')'

>>> a = Rational(1, 2)
>>> [str(a), repr(a)]
['1/2', 'Rational(1,2)']
>>> print(a)
1/2
>>> a
Rational(1,2)
```

### Q7: WWPD: Repr-esentation Q7： WWPD： Repr-esentation

Note: This is not the typical way `repr` is used, nor is this way of writing `repr` recommended, this problem is mainly just to make sure you understand how `repr` and `str` work.  
注意：这不是 `repr` 的典型使用方式，也不建议使用这种 `repr` 的编写方式，此问题主要只是为了确保您了解 `repr` 和 `str` 的工作原理。

```
class Car:
    def __init__(self, color):
        self.color = color

    def __repr__(self):
         return self.color

    def __str__(self):
         return self.color * 2

class Garage:
    def __init__(self):
         print('Vroom!')
         self.cars = []

    def add_car(self, car):
         self.cars.append(car)

    def __repr__(self):
         print(len(self.cars))
         ret = ''
         for car in self.cars:
             ret += str(car)
         return ret
```

Given the above class definitions, what will the following lines output?  
给定上述类定义，以下行将输出什么？

```
>>> Car('red')
```

```
>>> print(Car('red'))
```

```
>>> repr(Car('blue'))
```

```
>>> g = Garage()
```

```
>>> g.add_car(Car('red'))
>>> g.add_car(Car('blue'))
>>> g
```

### Q8: Cat Representation Q8： 猫代表

Now let's implement the `__str__` and `__repr__` methods for the `Cat` class from earlier so that they exhibit the following behavior:  
现在，让我们为前面的 `Cat` 类实现 `__str__` 和 `__repr__` 方法，以便它们表现出以下行为：

```
>>> cat = Cat("Felix", "Kevin")
>>> cat
Felix, 9 lives
>>> cat.lose_life()
>>> cat
Felix, 8 lives
>>> print(cat)
Felix
```

Enter to Rename, Shift+Enter to Preview

Run in 61A Code 在 61A 代码中运行