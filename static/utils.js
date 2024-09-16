export async function createTable({table_id = "#example-table", columns, data}) {
    var table = new Tabulator(table_id, {
        data: data,           // Используем полученные данные
        layout:"fitColumns",      //fit columns to width of table
        responsiveLayout:"hide",  //hide columns that don't fit on the table
        addRowPos:"top",          //when adding a new row, add it to the top of the table
        history:true,             //allow undo and redo actions on the table
        pagination:"local",       //paginate the data
        paginationSize:30,         //allow 7 rows per page of data
        paginationCounter:"rows", //display count of paginated rows in footer
        movableColumns:true,      //allow column order to be changed
        initialSort:[             //set the initial sort order of the data
            {column:"name", dir:"asc"},
        ],
        columnDefaults:{
            tooltip:true,         //show tool tips on cells
        },
        columns:columns
    });
    return table
}

export async function getTableData(url) {
    try {
        const response = await fetch(url, {
            headers: {
                'Content-Type': 'application/json'
            }
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();

        return data; // Возвращаем данные из функции
    } catch (e) {
        console.log(`Error while getting records from server! ${e.message}`);
        return []; // Возвращаем пустой массив в случае ошибки
    }
}

export async function refreshTableData(url) {
    const newData = await getTableData(url);
    table.replaceData(newData);  // Заменить все данные новыми
}

export function getDataFromTable(table) {
    var selectedData = table.getSelectedData(); //get array of currently selected data.
    console.log(selectedData)
    return selectedData
}

export function getLastActiveRow() {
    return lastActiveRow;
}