function getCheckedCheckBoxes() {
    let checkboxes = document.getElementsByClassName('checkbox');
    let checkboxesChecked = [];
  for (let index = 0; index < checkboxes.length; index++) {
     if (checkboxes[index].checked) {
        checkboxesChecked.push(checkboxes[index].value);
        alert(checkboxes[index].value);
     }
  }
  return checkboxesChecked;
}
console.log('static js')