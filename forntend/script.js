const API = "http://127.0.0.1:8000";

// REGISTER
if (document.getElementById("registerForm")) {
    document.getElementById("registerForm").onsubmit = async (e) => {
        e.preventDefault();

        let email = document.getElementById("email").value;
        let password = document.getElementById("password").value;

        let res = await fetch(`${API}/users/register`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email, password })
        });

        let msg = document.getElementById("msg");

        if (res.ok) {
            msg.innerText = "Registration successful! Go to Login page.";
        } else {
            msg.innerText = "Error registering user.";
        }
    };
}

// LOGIN
if (document.getElementById("loginForm")) {
    document.getElementById("loginForm").onsubmit = async (e) => {
        e.preventDefault();

        let email = document.getElementById("email").value;
        let password = document.getElementById("password").value;

        let res = await fetch(`${API}/users/login`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email, password })
        });

        let data = await res.json();
        let msg = document.getElementById("msg");

        if (data.access_token) {
            localStorage.setItem("token", data.access_token);
            window.location.href = "calculations.html";
        } else {
            msg.innerText = "Invalid credentials!";
        }
    };
}

// LOAD CALCULATIONS
async function loadCalculations() {
    const token = localStorage.getItem("token");
    if (!token) window.location.href = "login.html";

    let res = await fetch(`${API}/calculations/?token=${token}`);
    let data = await res.json();

    let listDiv = document.getElementById("list");
    listDiv.innerHTML = "";

    data.forEach(item => {
        listDiv.innerHTML += `
            <div>
                <b>ID:</b> ${item.id} — 
                ${item.operand1} ${item.operation} ${item.operand2} = ${item.result}
                <button onclick="deleteCalc(${item.id})">Delete</button>
            </div>
        `;
    });
}

// ADD CALCULATION
if (document.getElementById("addForm")) {
    document.getElementById("addForm").onsubmit = async (e) => {
        e.preventDefault();
        let token = localStorage.getItem("token");

        let operation = document.getElementById("operation").value;
        let operand1 = parseFloat(document.getElementById("operand1").value);
        let operand2 = parseFloat(document.getElementById("operand2").value);

        await fetch(`${API}/calculations/?token=${token}`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ operation, operand1, operand2 })
        });

        loadCalculations();
    };
}

// DELETE CALCULATION
async function deleteCalc(id) {
    let token = localStorage.getItem("token");

    await fetch(`${API}/calculations/${id}?token=${token}`, {
        method: "DELETE"
    });

    loadCalculations();
}

// LOGOUT
function logout() {
    localStorage.removeItem("token");
    window.location.href = "login.html";
}

// AUTOLOAD CALCULATIONS
if (window.location.href.endsWith("calculations.html")) {
    loadCalculations();
}
