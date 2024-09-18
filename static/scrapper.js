import { 
    createTable, 
    getTableData, 
    refreshTableData,
    getDataFromTable,

} from "./utils.js";

window.table = null

$(document).ready(async function() {
    console.log('Scrapper.js: Document ready!')
    table = await createTable({
        table_id: '#example-table',
        columns: [
            {formatter:"rowSelection", titleFormatter:"rowSelection", hozAlign:"center", headerSort:false, width:30},
            {title:"id", field:"id", visible: false},
            {title:"Domen", field:"domen", width:150},
            {title:"Link", field:"link", width:250},
            {title:"Handle", field:"handle", width:90,  hozAlign:"center", formatter:"tickCross", sorter:"boolean", editor:true, visible:false},
        ],
        data: await getTableData('/api/links'),
        initialFilter:[
            {field:"handle", type:"=", value:false},
        ],
    })

    table.setFilter("handle", "=", false);

    // ==============================================================> Buttons cliks
    // =====
    $('#create-task').click(() => {
        fetch('/scrapper-request', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                'search_request': $('#search-request').val(),
                'num': $('#num').val()
            })
        })
        .then(response => {
            return response.json().then(data => {
                if (!response.ok) {
                    // Handle non-ok responses (e.g., 4xx, 5xx)
                    throw new Error(data.message || `HTTP error: code ${response.status}`);
                }
                return data;
            });
        })
        .then(data => {
            console.log(data)
            console.log(`Command has been processed! ${data.message}`)
            refreshTableData('/api/links')
        })
        .catch(e => {
            console.log(`Error while creating task! ${e}`)
        })
    })

    $('#btn-transfer').click(() => {
        fetch('/scrapper-transfer', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                'links': getDataFromTable(table)
            })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Http error, status code: ' + response.status)
            } else {
                return response.json()
            }
        })
        .then(data => {
            console.log(data)
            refreshTableData('/api/links')
        })
        .catch(e => {
            alert(`Error on the route "/scrapper-transfer"`)
        })
    })
    // =====
    // ==============================================================> Buttons cliks

    // ==============================================================> Table events
    // =====
    table.on("rowSelectionChanged", function(data, rows, selected, deselected){
        //rows - array of row components for the currently selected rows in order of selection
        //data - array of data objects for the currently selected rows in order of selection
        //selected - array of row components that were selected in the last action
        //deselected - array of row components that were deselected in the last action
        if (data.length == 0) {
            $('#btn-transfer').text(`Transfer`)
        } else {
            $('#btn-transfer').text(`Transfer (${data.length})`)
        }
    });


    // =====
    // ==============================================================> Table events

})
