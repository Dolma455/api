<!DOCTYPE html>
<html>
<head>
  <title>Mark Entry - <?php echo $_GET['subject']; ?></title>
  <link rel="stylesheet" type="text/css" href="classsubject.css">
</head>
<body>
  <h1>Mark Entry - <?php echo $_GET['subject']; ?></h1>

  <form id="mark_entry_form" action="save-marks.php" method="post">
    <label for="num_students">Number of Students:</label>
    <input type="number" id="num_students" name="num_students" min="1" required>

    <button type="button" onclick="generateTable()">Generate Table</button>

    <div id="table_container" style="display: none;">
      <table id="mark_entry_table">
        <thead>
          <tr>
            <th>SN</th>
            <th>Student Name</th>
            <th>Theory Marks</th>
            <th>Practical Marks</th>
            <th>Total Marks</th>
          </tr>
        </thead>
        <tbody id="table_body"></tbody>
      </table>

      <button type="submit">Save</button>
    </div>
  </form>

  <script>
    function generateTable() {
      var numStudents = parseInt(document.getElementById("num_students").value);
      var tableBody = document.getElementById("table_body");
      tableBody.innerHTML = "";

      for (var i = 1; i <= numStudents; i++) {
        var row = document.createElement("tr");

        var snCell = document.createElement("td");
        snCell.textContent = i;
        row.appendChild(snCell);

        var nameCell = document.createElement("td");
        var nameInput = document.createElement("input");
        nameInput.type = "text";
        nameInput.name = "student_name[]";
        nameCell.appendChild(nameInput);
        row.appendChild(nameCell);

        var theoryCell = document.createElement("td");
        var theoryInput = document.createElement("input");
        theoryInput.type = "number";
        theoryInput.name = "theory_marks[]";
        theoryCell.appendChild(theoryInput);
        row.appendChild(theoryCell);

        var practicalCell = document.createElement("td");
        var practicalInput = document.createElement("input");
        practicalInput.type = "number";
        practicalInput.name = "practical_marks[]";
        practicalCell.appendChild(practicalInput);
        row.appendChild(practicalCell);

        var totalCell = document.createElement("td");
        var totalInput = document.createElement("input");
        totalInput.type = "number";
        totalInput.name = "total_marks[]";
        totalInput.readOnly = true;
        totalCell.appendChild(totalInput);
        row.appendChild(totalCell);

        tableBody.appendChild(row);
      }

      var tableContainer = document.getElementById("table_container");
      tableContainer.style.display = "block";
    }
  </script>
</body>
</html>
