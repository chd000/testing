(function ($) {
    $(document).on("click", "#nextButton", function () {
        $.ajax({
            type: "GET",
            url: 'http://127.0.0.1:8000/result',
            data: {
                list: getCheckedCheckBoxes()
            },
            dataType: 'json',
            success: function () {
            }
        })
        alert('Ваши ответы отправлены, нажмите "Завершить тест"')
        location.href = 'http://127.0.0.1:8000/result'
    })
})(jQuery);

document.getElementById('myselect').addEventListener('change', function () {
    let getValue = this.value;
    console.log(getValue);
});

function getValue() {
    let select = document.getElementById('myselect');
    let value = select.value;
    console.log(value);
}

function getCheckedCheckBoxes() {
    let checkboxes = document.getElementsByClassName('checkbox');
    let checkboxesChecked = [];
    for (let index = 0; index < checkboxes.length; index++) {
        if (checkboxes[index].checked) {
            checkboxesChecked.push(checkboxes[index].value);
        }
    }
    console.log(checkboxesChecked)
    return checkboxesChecked;
}