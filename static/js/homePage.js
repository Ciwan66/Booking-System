document.addEventListener('DOMContentLoaded', function() {
    const toggleMenu = document.querySelector('.toggle-menu');
    const menu = document.querySelector('nav ul');

    toggleMenu.addEventListener('click', function() {
        menu.classList.toggle('active');
    });
});
// -------------------------------------------------------------------


// Sample array of destinations
let destinations = [];

function populateDestinations() {
    let inputCity = $("#inputCity");

    destinations.forEach(function(destination) {
        let option = new Option(destination, destination);
        inputCity.append(option);
    });

    inputCity.select2();
}

populateDestinations();
// -------------------------------------------------------------------
document.getElementById('minPrice').addEventListener('input', validatePrices);
document.getElementById('maxPrice').addEventListener('input', validatePrices);

function validatePrices() {
    let minPrice = parseFloat(document.getElementById('minPrice').value);
    let maxPrice = parseFloat(document.getElementById('maxPrice').value);

    let errorMessage = '';

    if (minPrice <= 0 || maxPrice <= 0) {
        errorMessage = 'Prices must be greater than zero.';
    } else if (maxPrice < minPrice) {
        errorMessage = 'Maximum price must be greater than or equal to minimum price.';
    }

    document.getElementById('error-message').textContent = errorMessage;
}
// ---------------------------------------------------------------------
$(function() {
    // Set minimum date for check-in
    let today = new Date();
    let month = today.getMonth() + 1;
    let day = today.getDate();
    let year = today.getFullYear();
    if (month < 10) {
        month = '0' + month.toString();
    }
    if (day < 10) {
        day = '0' + day.toString();
    }
    let minDate = year + '-' + month + '-' + day;
    $('.checkInDate').attr('min', minDate);

    // Set minimum and maximum date for check-out
    $('.checkInDate').on('change', function() {
        let checkInDate = new Date($(this).val());
        checkInDate.setDate(checkInDate.getDate() + 1); // Add one day to check-in date
        
        let checkOutMinDate = checkInDate.toISOString().split('T')[0];
        $('.checkOutDate').attr('min', checkOutMinDate);

        let oneYearAndOneDayLater = new Date(today);
        oneYearAndOneDayLater.setFullYear(oneYearAndOneDayLater.getFullYear() + 1);
        oneYearAndOneDayLater.setDate(oneYearAndOneDayLater.getDate() + 1); // Add one more day for maximum
        let maxDate = oneYearAndOneDayLater.toISOString().split('T')[0];
        $('.checkOutDate').attr('max', maxDate);
    });
});

// Set maximum date for check-in
$(function() {
    let today = new Date();
    let oneYearLater = new Date(today);
    oneYearLater.setFullYear(oneYearLater.getFullYear() + 1);

    let month = oneYearLater.getMonth() + 1;
    let day = oneYearLater.getDate();
    let year = oneYearLater.getFullYear();

    if (month < 10) {
        month = '0' + month.toString();
    }
    if (day < 10) {
        day = '0' + day.toString();
    }

    let maxDate = year + '-' + month + '-' + day;
    $('.checkInDate').attr('max', maxDate);

});
// ----------------------------------------------------------------------------
    // carousels
$(function() {
    $('.carousel').carousel ({
        interval: 1000
    });
})
    // carousels