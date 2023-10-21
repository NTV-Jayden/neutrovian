document.addEventListener("DOMContentLoaded", function () {
    var duration = 5000;
    var interval = 1000;

    if (document.getElementById('div') && document.getElementById('div').innerText.trim() !== '') {
        var countdown = duration / interval;

        var timerId = setInterval(function () {
            console.log(`Removing message in ${countdown} seconds`);
            countdown--;

            if (countdown < 0) {
                clearInterval(timerId);
                var elem = document.getElementById('div');
                if (elem) {
                    elem.style.display = 'none';
                }
            }
        }, interval);
    }
});
