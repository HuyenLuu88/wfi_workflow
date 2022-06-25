let table = $('#datatables').DataTable({
    "processing": true,
        "language": {
            processing: '<i class="fa fa-spinner fa-spin fa-3x fa-fw"></i><span class="sr-only">Loading...</span> '},
    "serverSide": true,

    "ajax": {
        "url": "/api/portfolio/",
        "type": "GET"
    },
       "columnDefs": [{
       "targets": [6],
       "orderable": false,
           'className': 'select-checkbox',
            'checkboxes': {
                'selectRow': true
                }
        }],

        'select': {
                    'style': 'multi',
                },

        "columns": [
            {"data": "id"},
            {"data": "code"},
            {"data": "type"},
            {"data": "created"},
            {"data": "updated"},
            {"data": "valid"},
            {
                "data": null,
                "defaultContent": '<button type="button" class="btn btn-info">Edit</button>' + '&nbsp;&nbsp' +
                '<button type="button" class="btn btn-danger">Delete</button>'
            }
        ],



    // dom: 'Bfrtip',
    //     buttons: [
    //         'copyHtml5',
    //         'excelHtml5',
    //         'csvHtml5',
    //         'pdfHtml5'
    //     ],
});

let id = 0;

$('#datatables tbody').on('click', 'button', function () {
    let data = table.row($(this).parents('tr')).data();
    let class_name = $(this).attr('class');
    if (class_name == 'btn btn-info') {
        // EDIT button
        $('#code').val(data['code']);
        //$('#valid').val(data['valid']);
        $('#type').val('edit');
        $('#modal_title').text('EDIT');
        $("#myModal").modal();
    } else {
        // DELETE button
        $('#modal_title').text('DELETE');
        $("#confirm").modal();
    }

    id = data['id'];

});

$('form').on('submit', function (e) {
    e.preventDefault();
    let $this = $(this);
    let type = $('#type').val();
    let method = '';
    let url = '/api/portfolio/';
    if (type == 'new') {
        // new
        method = 'POST';
    } else {
        // edit
        url = url + id + '/';
        method = 'PUT';
    }

    $.ajax({
        url: url,
        method: method,
        data: $this.serialize()
    }).success(function (data, textStatus, jqXHR) {
        location.reload();
    }).error(function (jqXHR, textStatus, errorThrown) {
        console.log(jqXHR)
    });
});

$('#confirm').on('click', '#delete', function (e) {
    $.ajax({
        url: '/api/portfolio/' + id + '/',
        method: 'DELETE'
    }).success(function (data, textStatus, jqXHR) {
        location.reload();
    }).error(function (jqXHR, textStatus, errorThrown) {
        console.log(jqXHR)
    });
});


$('#new').on('click', function (e) {
    $('#code').val('');
    //$('#valid').val('');
    $('#type').val('new');
    $('#modal_title').text('NEW');
    $("#myModal").modal();
});


