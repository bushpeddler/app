document.addEventListener("DOMContentLoaded", function () {
    // 📈 Fetch market data
    fetch("/api/market")
        .then(response => response.json())
        .then(data => {
            let labels = data.map(item => item.stock);
            let prices = data.map(item => item.price);

            new Chart(document.getElementById("marketChart"), {
                type: "bar",
                data: {
                    labels: labels,
                    datasets: [{
                        label: "Stock Prices",
                        backgroundColor: "rgba(0, 255, 204, 0.6)",
                        data: prices
                    }]
                }
            });
        });

    // 💰 Fetch player rankings
    fetch("/api/players")
        .then(response => response.json())
        .then(data => {
            let playerList = document.getElementById("playerList");
            data.forEach(player => {
                let li = document.createElement("li");
                li.textContent = `${player.username}: ${player.wealth} credits`;
                playerList.appendChild(li);
            });
        });

    // 🎭 Fetch faction influence
    fetch("/api/factions")
        .then(response => response.json())
        .then(data => {
            let labels = data.map(item => item.faction);
            let counts = data.map(item => item.count);

            new Chart(document.getElementById("factionChart"), {
                type: "pie",
                data: {
                    labels: labels,
                    datasets: [{
                        label: "Faction Influence",
                        backgroundColor: ["#ff5733", "#33c4ff", "#33ff57"],
                        data: counts
                    }]
                }
            });
        });
});