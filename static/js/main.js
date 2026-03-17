
function newEvent() {
    const name = document.getElementById("new_event_name").value;
    fetch(`/events/${name}/`, { method: "PUT" })
        .then(r => r.json())
        .then(data => {
            console.log(data);
            location.reload();
        });
}

function addEvent(name) {
    fetch(`/events/${name}/`, { method: "POST" })
        .then(r => r.json())
        .then(data => {
            console.log(data);
            location.reload();
        });
}

document.getElementById("new_event_name").addEventListener("keydown", function(e) {
    if (e.key === "Enter") newEvent();
});
