const API = "http://127.0.0.1:5000";

function addExpense() {
    let amount = document.getElementById("amount").value;
    let category = document.getElementById("category").value;
    let date = document.getElementById("date").value;

    if (amount === "" || category === "" || date === "") {
        alert("Fill all fields");
        return;
    }

    fetch(API + "/add", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            amount: amount,
            category: category,
            date: date
        })
    }).then(() => {
        loadExpenses();
        document.getElementById("amount").value = "";
        document.getElementById("category").value = "";
        document.getElementById("date").value = "";
    });
}

function loadExpenses() {
    fetch(API + "/expenses")
        .then(res => res.json())
        .then(data => {
            let list = document.getElementById("expenseList");
            let total = 0;
            list.innerHTML = "";

            data.forEach(e => {
                total += e.amount;
                let item = document.createElement("li");
                item.innerText = `${e.date} | ${e.category} | ₹${e.amount}`;
                list.appendChild(item);
            });

            document.getElementById("total").innerText = "Total: ₹" + total;
        });
}

loadExpenses();
