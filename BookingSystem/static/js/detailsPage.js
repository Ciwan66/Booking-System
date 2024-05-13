
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
// Set minimum date for check-in
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

  // Set maximum date for check-in
  var oneYearLater = new Date(today);
  oneYearLater.setFullYear(oneYearLater.getFullYear() + 1);

  var month = oneYearLater.getMonth() + 1;
  var day = oneYearLater.getDate();
  var year = oneYearLater.getFullYear();

  if (month < 10) {
      month = '0' + month.toString();
  }
  if (day < 10) {
      day = '0' + day.toString();
  }

  var maxCheckInDate = year + '-' + month + '-' + day;
  $('.checkInDate').attr('max', maxCheckInDate);

  // Adjusted booked dates with check-in and check-out dates as objects

  $('.checkInDate').datepicker({
      dateFormat: 'yy-mm-dd',
      minDate: minDate,
      maxDate: maxCheckInDate,
      beforeShowDay: function(date) {
          var dateString = $.datepicker.formatDate('yy-mm-dd', date);
          for (var i = 0; i < bookedDates.length; i++) {
              var checkIn = new Date(bookedDates[i].checkIn);
              var checkOut = new Date(bookedDates[i].checkOut);
              if (date >= checkIn && date <= checkOut) {
                  // Disable booked dates and days between them
                  if (date.getTime() >= checkIn.getTime() && date.getTime() <= checkOut.getTime()) {
                      return [false, 'booked-date', 'Booked'];
                  } else {
                      return [true, ''];
                  }
              }
              // Check if the current date is the check-in date itself, and disable it
              if (dateString === bookedDates[i].checkIn) {
                  return [false, 'booked-date', 'Booked'];
              }
          }
          return [true, ''];
      },
      onSelect: function(selectedDate) {
          var checkInDate = $(this).datepicker('getDate');
          checkInDate.setDate(checkInDate.getDate() + 1); // Add one day to check-in date
          
          var checkOutMinDate = formatDate(checkInDate);
          $('.checkOutDate').datepicker('option', 'minDate', checkOutMinDate);

          var maxCheckOutDate = new Date(oneYearLater);
          var foundDisabledDate = false;
          for (var i = 0; i < bookedDates.length; i++) {
              var disabledDate = new Date(bookedDates[i].checkOut);
              if (disabledDate > checkInDate) {
                  maxCheckOutDate = new Date(disabledDate);
                  maxCheckOutDate.setDate(maxCheckOutDate.getDate() - 1); // Set max date to the day before the first disabled date after the check-in date
                  foundDisabledDate = true;
                  break;
              }
          }
          if (!foundDisabledDate) {
              maxCheckOutDate = new Date(oneYearLater);
              maxCheckOutDate.setDate(maxCheckOutDate.getDate() + 1); // Set max date to one year and one day from the current date
          }
          var maxCheckOutDateString = formatDate(maxCheckOutDate);
          $('.checkOutDate').datepicker('option', 'maxDate', maxCheckOutDateString);
      }
  });

  $('.checkOutDate').datepicker({
      dateFormat: 'yy-mm-dd',
      minDate: minDate,
      beforeShowDay: function(date) {
          var dateString = $.datepicker.formatDate('yy-mm-dd', date);
          for (var i = 0; i < bookedDates.length; i++) {
              var checkIn = new Date(bookedDates[i].checkIn);
              var checkOut = new Date(bookedDates[i].checkOut);
              if (date >= checkIn && date <= checkOut) {
                  // Disable booked dates and days between them
                  if (date.getTime() >= checkIn.getTime() && date.getTime() <= checkOut.getTime()) {
                      return [false, 'booked-date', 'Booked'];
                  } else {
                      return [true, ''];
                  }
              }
              // Check if the current date is the check-in date itself, and disable it
              if (dateString === bookedDates[i].checkIn) {
                  return [false, 'booked-date', 'Booked'];
              }
          }
          return [true, ''];
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
