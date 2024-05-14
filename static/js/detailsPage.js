
document.addEventListener("DOMContentLoaded", function() {
    let imgsContainer = document.querySelector('.imgs');

    let currentRow;

    images.forEach((image, index) => {
        // Create a new row for every third image or at the start
        if (index % 3 === 0) {
            currentRow = document.createElement('div');
            currentRow.className = 'row';
            imgsContainer.appendChild(currentRow);
        }

        let col = document.createElement("div");
        col.className = "col-md-4";

        let img = document.createElement("img");
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

// Function to generate stars dynamically based on a letiable value
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
// Example usage: Replace 3.5 with your dynamic letiable value

let starsContainer = document.getElementById('stars');
starsContainer.innerHTML = generateStars(rating);


// ------------------------------------------------------------
// Set minimum date for check-in
$(document).ready(function() {

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

  // Set maximum date for check-in
  let oneYearLater = new Date(today);
  oneYearLater.setFullYear(oneYearLater.getFullYear() + 1);

  let month2 = oneYearLater.getMonth() + 1;
  let day2 = oneYearLater.getDate();
  let year2 = oneYearLater.getFullYear();

  if (month2 < 10) {
      month2 = '0' + month.toString();
  }
  if (day2 < 10) {
      day2 = '0' + day2.toString();
  }

  let maxCheckInDate = year2 + '-' + month2 + '-' + day2;
  $('.checkInDate').attr('max', maxCheckInDate);

  // Adjusted booked dates with check-in and check-out dates as objects

  $('.checkInDate').datepicker({
      dateFormat: 'yy-mm-dd',
      minDate: minDate,
      maxDate: maxCheckInDate,
      beforeShowDay: function(date) {
          let dateString = $.datepicker.formatDate('yy-mm-dd', date);
          for (const element of bookedDates) {
              let checkIn = new Date(element.checkIn);
              let checkOut = new Date(element.checkOut);
              if (date >= checkIn && date <= checkOut) {
                  // Disable booked dates and days between them
                  if (date.getTime() >= checkIn.getTime() && date.getTime() <= checkOut.getTime()) {
                      return [false, 'booked-date', 'Booked'];
                  } else {
                      return [true, ''];
                  }
              }
              // Check if the current date is the check-in date itself, and disable it
              if (dateString === element.checkIn) {
                  return [false, 'booked-date', 'Booked'];
              }
          }
          return [true, ''];
      },
      onSelect: function(selectedDate) {
          let checkInDate = $(this).datepicker('getDate');
          checkInDate.setDate(checkInDate.getDate() + 1); // Add one day to check-in date
          
          let checkOutMinDate = formatDate(checkInDate);
          $('.checkOutDate').datepicker('option', 'minDate', checkOutMinDate);

          let maxCheckOutDate = new Date(oneYearLater);
          let foundDisabledDate = false;
          for (const element of bookedDates) {
              let disabledDate = new Date(element.checkOut);
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
          let maxCheckOutDateString = formatDate(maxCheckOutDate);
          $('.checkOutDate').datepicker('option', 'maxDate', maxCheckOutDateString);
      }
  });

  $('.checkOutDate').datepicker({
      dateFormat: 'yy-mm-dd',
      minDate: minDate,
      beforeShowDay: function(date) {
        let dateString = $.datepicker.formatDate('yy-mm-dd', date);
          for (const element of bookedDates) {
            let checkIn = new Date(element.checkIn);
              let checkOut = new Date(element.checkOut);
              if (date >= checkIn && date <= checkOut) {
                  // Disable booked dates and days between them
                  if (date.getTime() >= checkIn.getTime() && date.getTime() <= checkOut.getTime()) {
                      return [false, 'booked-date', 'Booked'];
                  } else {
                      return [true, ''];
                  }
              }
              // Check if the current date is the check-in date itself, and disable it
              if (dateString === element.checkIn) {
                  return [false, 'booked-date', 'Booked'];
              }
          }
          return [true, ''];
      }
  });

  function formatDate(date) {
    let month = date.getMonth() + 1;
      let day = date.getDate();
      let year = date.getFullYear();
      if (month < 10) {
          month = '0' + month.toString();
      }
      if (day < 10) {
          day = '0' + day.toString();
      }
      return year + '-' + month + '-' + day;
  }
});
