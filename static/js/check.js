function checkedId() {
    let checkboxes = document.getElementsByClassName('checkbox');
    let checkedId = []
    for (let k = 0; k < checkboxes.length; k++) {
        if (checkedId.indexOf(checkboxes[k].id) === -1) {
            checkedId.push(checkboxes[k].id)
        }
    }
    return checkedId
}

function getCheckedCheckBoxes() {
    let checkboxes = document.getElementsByClassName('checkbox');
    let checkboxesChecked = [];

    for (let i = 0; i < 20; i++) {
        let checkboxesList = []
        checkboxesChecked.push(checkboxesList)
    }
    for (let index = 0; index < checkboxes.length; index++) {
        if (checkboxes[index].checked) {
            for (let j = 0; j < checkedId().length; j++) {
                if (checkboxes[index].id === checkedId()[j]) {
                    checkboxesChecked[j].splice(j, 0, checkboxes[index].value)
                }
            }
        }
    }
    console.log(checkboxesChecked)
    return checkboxesChecked;
}