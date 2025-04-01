// Завдання 1
function task1() {
    let fruits = ["яблуко", "банан", "апельсин", "виноград"];
    console.log("Завдання 1:");
    console.log("Початковий масив:", fruits);

    fruits.pop();
    console.log("Після видалення останнього елемента:", fruits);

    fruits.unshift("ананас");
    console.log("Після додавання 'ананас' на початок:", fruits);

    fruits.sort().reverse();
    console.log("Відсортований у зворотньому алфавітному порядку:", fruits);

    let index = fruits.indexOf("яблуко");
    console.log("Індекс 'яблуко':", index);
}

// Завдання 2
function task2() {
    let colors = ["червоний", "зелений", "синій", "жовтий", "фіолетовий", "темно-синій"];
    console.log("Завдання 2:");
    console.log("Початковий масив:", colors);

    let longest = colors.reduce((a, b) => a.length > b.length ? a : b);
    let shortest = colors.reduce((a, b) => a.length < b.length ? a : b);
    console.log("Найдовший колір:", longest);
    console.log("Найкоротший колір:", shortest);

    let blueColors = colors.filter(color => color.includes("синій"));
    console.log("Кольори, що містять 'синій':", blueColors);

    let joined = blueColors.join(",");
    console.log("Об’єднаний рядок:", joined);
}

// Завдання 3
function task3() {
    let employees = [
        { name: "Іван", age: 30, position: "розробник" },
        { name: "Петро", age: 25, position: "дизайнер" },
        { name: "Марія", age: 28, position: "розробник" }
    ];
    console.log("Завдання 3:");
    console.log("Початковий масив:", employees);

    employees.sort((a, b) => a.name.localeCompare(b.name));
    console.log("Відсортований за іменами:", employees);

    let developers = employees.filter(emp => emp.position === "розробник");
    console.log("Розробники:", developers);

    employees = employees.filter(emp => emp.age <= 28);
    console.log("Після видалення працівників старше 28:", employees);

    employees.push({ name: "Олена", age: 27, position: "менеджер" });
    console.log("Після додавання нового працівника:", employees);
}

// Завдання 4
function task4() {
    let students = [
        { name: "Олексій", age: 20, course: 2 },
        { name: "Анна", age: 19, course: 1 },
        { name: "Дмитро", age: 21, course: 3 }
    ];
    console.log("Завдання 4:");
    console.log("Початковий масив:", students);

    students = students.filter(student => student.name !== "Олексій");
    console.log("Після видалення 'Олексій':", students);

    students.push({ name: "Ірина", age: 22, course: 4 });
    console.log("Після додавання нового студента:", students);

    students.sort((a, b) => b.age - a.age);
    console.log("Відсортовані за віком від найстаршого:", students);

    let thirdCourseStudent = students.find(student => student.course === 3);
    console.log("Студент на 3-му курсі:", thirdCourseStudent);
}

// Завдання 5
function task5() {
    let numbers = [1, 2, 3, 4, 5];
    console.log("Завдання 5:");
    console.log("Початковий масив:", numbers);

    let squares = numbers.map(num => num * num);
    console.log("Квадрати чисел:", squares);

    let evens = numbers.filter(num => num % 2 === 0);
    console.log("Парні числа:", evens);

    let sum = numbers.reduce((acc, num) => acc + num, 0);
    console.log("Сума чисел:", sum);

    let newNumbers = [6, 7, 8, 9, 10];
    numbers = numbers.concat(newNumbers);
    console.log("Після додавання нового масиву:", numbers);

    numbers.splice(0, 3);
    console.log("Після видалення перших 3 елементів:", numbers);
}

// Завдання 6
function libraryManagement() {
    let books = [
        { title: "Книга1", author: "Автор1", genre: "Жанр1", pages: 100, isAvailable: true },
        { title: "Книга2", author: "Автор2", genre: "Жанр2", pages: 200, isAvailable: false },
        { title: "Книга3", author: "Автор1", genre: "Жанр3", pages: 150, isAvailable: true }
    ];

    function addBook(title, author, genre, pages) {
        books.push({ title, author, genre, pages, isAvailable: true });
    }

    function removeBook(title) {
        books = books.filter(book => book.title !== title);
    }

    function findBooksByAuthor(author) {
        return books.filter(book => book.author === author);
    }

    function toggleBookAvailability(title, isBorrowed) {
        let book = books.find(book => book.title === title);
        if (book) {
            book.isAvailable = !isBorrowed;
        }
    }

    function sortBooksByPages() {
        books.sort((a, b) => a.pages - b.pages);
    }

    function getBooksStatistics() {
        let totalBooks = books.length;
        let availableBooks = books.filter(book => book.isAvailable).length;
        let borrowedBooks = totalBooks - availableBooks;
        let totalPages = books.reduce((acc, book) => acc + book.pages, 0);
        let averagePages = totalBooks > 0 ? totalPages / totalBooks : 0;
        return {
            totalBooks,
            availableBooks,
            borrowedBooks,
            averagePages
        };
    }

    console.log("Завдання 6:");
    console.log("Початковий масив книг:", books);

    addBook("Книга4", "Автор3", "Жанр4", 250);
    console.log("Після додавання нової книги:", books);

    removeBook("Книга2");
    console.log("Після видалення 'Книга2':", books);

    let authorBooks = findBooksByAuthor("Автор1");
    console.log("Книги автора 'Автор1':", authorBooks);

    toggleBookAvailability("Книга1", true);
    console.log("Після взяття 'Книга1':", books);

    sortBooksByPages();
    console.log("Відсортовані за кількістю сторінок:", books);

    let stats = getBooksStatistics();
    console.log("Статистика:", stats);
}

// Завдання 7
function task7() {
    let student = { name: "Студент", age: 20, course: 2 };
    console.log("Завдання 7:");
    console.log("Початковий об’єкт:", student);

    student.subjects = ["Математика", "Фізика"];
    console.log("Після додавання subjects:", student);

    delete student.age;
    console.log("Після видалення age:", student);
}


task1();
task2();
task3();
task4();
task5();
libraryManagement();
task7();