let currentReceiver = null;
let currentCourse = null;
let isGroupChat = false;

let socket = null;

// -----------------------------
// Load Users
// -----------------------------
function loadUsers(users) {

    const list = document.getElementById("user-list");

    list.innerHTML = "";

    // Group Chat
    list.innerHTML += `
        <div class="user-item"
             onclick="selectGroup(1,'Python Programming Group')">

            <strong>📢 Python Programming Group</strong><br>
            <small>Group Chat</small>

        </div>
    `;

    users.forEach(user => {

        if (user.id === currentUserId) return;

        const status = user.online
            ? "<span style='color:lime;'>● Online</span>"
            : "<span style='color:red;'>● Offline</span>";

        list.innerHTML += `
            <div class="user-item"
                 onclick="selectUser(${user.id}, '${user.full_name}')">

                <strong>${user.full_name}</strong><br>
                <small>${user.role}</small><br>

                ${status}

            </div>
        `;
    });

}

function fetchUsers() {

    fetch("http://127.0.0.1:8001/chat/users")
        .then(response => response.json())
        .then(users => loadUsers(users));

}

// -----------------------------
// WebSocket
// -----------------------------
function connectSocket() {

    socket = new WebSocket(
        `ws://127.0.0.1:8001/ws/chat/${currentUserId}`
    );

    socket.onopen = function () {

        console.log("WebSocket Connected");

    };

    socket.onclose = function () {

        console.log("WebSocket Closed");

        setTimeout(connectSocket, 1000);

    };

    socket.onerror = function (e) {

        console.log(e);

    };

    socket.onmessage = function (event) {

        const data = JSON.parse(event.data);
        // Notification
if (!data.is_group && Number(data.receiver_id) === Number(currentUserId)) {

    alert("🔔 New message received!");

}

        console.log(data);

        // Online / Offline refresh
        if (data.type === "online_users") {

            fetchUsers();

            return;

        }

        if (!data.message) return;

        // Group Chat
        if (data.is_group && isGroupChat) {

            const chatBox = document.getElementById("chat-box");

            chatBox.innerHTML += `
                <div class="message">

                    <div class="sender">
                        User ${data.sender_id}
                    </div>

                    <div class="text">
                        ${data.message}
                    </div>

                </div>
            `;

            chatBox.scrollTop = chatBox.scrollHeight;

            return;

        }

        // Private Chat

        if (
            Number(data.sender_id) !== Number(currentReceiver) &&
            Number(data.receiver_id) !== Number(currentReceiver)
        ) {
            return;
        }

        const title = document.querySelector("h5");

        if (title) {

            selectUser(currentReceiver, title.innerText);

        }

    };

}

connectSocket();

fetchUsers();

// -----------------------------
// Private Chat
// -----------------------------
function selectUser(id, name) {

    currentReceiver = id;
    currentCourse = null;
    isGroupChat = false;

    const chatBox = document.getElementById("chat-box");

    chatBox.innerHTML = `
        <h5>${name}</h5>
        <hr>
    `;

    fetch(
        `http://127.0.0.1:8001/chat/history/${currentUserId}/${id}`
    )
    .then(response => response.json())
    .then(messages => {

        messages.forEach(msg => {

            const mine = msg.sender_id === currentUserId;

            chatBox.innerHTML += `
                <div class="${mine ? 'my-message' : 'message'}">

                    <div class="sender">
                        ${mine ? "You" : name}
                    </div>

                    <div class="text">
                        ${msg.message}
                    </div>

                </div>
            `;

        });

        chatBox.scrollTop = chatBox.scrollHeight;

    });

}

// -----------------------------
// Group Chat
// -----------------------------
function selectGroup(courseId, name) {

    currentCourse = courseId;
    currentReceiver = null;
    isGroupChat = true;

    document.getElementById("chat-box").innerHTML = `
        <h5>📢 ${name}</h5>
        <hr>
    `;

}

// -----------------------------
// Send Message
// -----------------------------
function sendMessage() {

    const input = document.getElementById("message");

    if (input.value.trim() === "") {

        return;

    }

    let payload;

    if (isGroupChat) {

        payload = {

            course_id: currentCourse,
            message: input.value,
            is_group: true

        };

    } else {

        if (currentReceiver === null) {

            alert("Select a user first.");

            return;

        }

        payload = {

            receiver_id: currentReceiver,
            message: input.value,
            is_group: false

        };

    }

    if (socket.readyState !== WebSocket.OPEN) {

        alert("WebSocket disconnected");

        return;

    }

    socket.send(JSON.stringify(payload));

    input.value = "";

}