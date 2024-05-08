// // images
// document.addEventListener("DOMContentLoaded", function() {
//     const images = ["../images/1.jpg", "../images/2.jpg", "../images/3.jpg","../images/2.jpg", "../images/3.jpg"];
//     const imgsContainer = document.querySelector('.imgs');

//     let currentRow;

//     images.forEach((image, index) => {
//         // Create a new row for every third image or at the start
//         if (index % 3 === 0) {
//             currentRow = document.createElement('div');
//             currentRow.className = 'row';
//             imgsContainer.appendChild(currentRow);
//         }

//         const col = document.createElement("div");
//         col.className = "col-md-4";

//         const img = document.createElement("img");
//         img.src = image;
//         img.alt = "Apartment Image";

//         col.appendChild(img);
//         currentRow.appendChild(col);
//     });
// });
document.addEventListener("DOMContentLoaded", function() {
    const imgsContainer = document.querySelector('.imgs');

    let currentRow;

    images.forEach((image, index) => {
        // Create a new row for every third image or at the start
        if (index % 3 === 0) {
            currentRow = document.createElement('div');
            currentRow.className = 'row';
            imgsContainer.appendChild(currentRow);
        }

        const col = document.createElement("div");
        col.className = "col-md-4";

        const img = document.createElement("img");
        img.src = image;
        img.alt = "Apartment Image";
        img.classList.add('expandable-image'); // Add a class for handling expansion

        // Add click event listener to each image
        img.addEventListener('click', function() {
            img.classList.toggle('expanded');
        });

        col.appendChild(img);
        currentRow.appendChild(col);
    });
});

// ---------------------------------------------------------------

// Function to generate stars dynamically based on a variable value
function generateStars(rating) {
    let starsHTML = '';
    for (let i = 1; i <= 5; i++) {
        if (i <= rating) {
            starsHTML += '<i class="fas fa-star starColor"></i>';
        } else if (i - rating == 0.5) {
            starsHTML += '<i class="fas fa-star-half-alt starColor"></i>';
        } else {
            starsHTML += '<i class="far fa-star starColor"></i>';
        }
    }
    return starsHTML;
}
// Example usage: Replace 3.5 with your dynamic variable value

const starsContainer = document.getElementById('stars');
starsContainer.innerHTML = generateStars(rating);


// ------------------------------------------------------------
$(document).ready(function() {
    var today = new Date();
    var month = today.getMonth() + 1;
    var day = today.getDate();
    var year = today.getFullYear();
    if (month < 10) {
      month = '0' + month.toString();
    }
    if (day < 10) {
      day = '0' + day.toString();
    }
    var minDate = year + '-' + month + '-' + day;
    $('.checkInDate').attr('min', minDate);
  
    var oneYearLater = new Date(today);
    oneYearLater.setFullYear(oneYearLater.getFullYear() + 1);
  
    month = oneYearLater.getMonth() + 1;
    day = oneYearLater.getDate();
    year = oneYearLater.getFullYear();
  
    if (month < 10) {
      month = '0' + month.toString();
    }
    if (day < 10) {
      day = '0' + day.toString();
    }
  
    var maxCheckInDate = year + '-' + month + '-' + day;
  
    // Disable booked dates for check-in
  
    $('.checkInDate').datepicker({
      dateFormat: 'yy-mm-dd',
      minDate: minDate,
      maxDate: maxCheckInDate,
      beforeShowDay: function(date) {
        var dateString = $.datepicker.formatDate('yy-mm-dd', date);
        return [bookedDates.indexOf(dateString) == -1, '']; // Check for booked dates
      },
      onSelect: function(selectedDate) {
        var checkInDate = $(this).datepicker('getDate');
        var checkOutMinDate = formatDate(checkInDate.setDate(checkInDate.getDate() + 1)); // Add one day to check-in for min checkout date
        
        $('.checkOutDate').datepicker('option', 'minDate', checkOutMinDate);
  
        // Disable dates between check-in and potential check-out
        var maxCheckOutDate = new Date(oneYearLater);
        $('.checkOutDate').datepicker({
          beforeShowDay: function(date) {
            var dateString = $.datepicker.formatDate('yy-mm-dd', date);
            if (date < checkInDate || date > maxCheckOutDate) {
              return [false, '']; // Disable dates before check-in or after potential checkout
            }
            return [bookedDates.indexOf(dateString) == -1, '']; // Check for booked dates within valid range
          }
        });
      }
    });
  
    $('.checkOutDate').datepicker({
      dateFormat: 'yy-mm-dd',
      minDate: minDate,
      beforeShowDay: function(date) {
        var dateString = $.datepicker.formatDate('yy-mm-dd', date);
        return [bookedDates.indexOf(dateString) == -1, '']; // Check for booked dates
      }
    });
  
    function formatDate(date) {
      var month = date.getMonth() + 1;
      var day = date.getDate();
      var year = date.getFullYear();
      if (month < 10) {
        month = '0' + month.toString();
      }
      if (day < 10) {
        day = '0' + day.toString();
      }
      return year + '-' + month + '-' + day;
    }
  });