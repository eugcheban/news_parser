import { 
    createTable, 
    getTableData, 
    refreshTableData, 
    getLastActiveRow 
} from "./utils.js";

window.last_clicked_row = {}
window.table = undefined
window.editor = undefined
window.postEditor = undefined

var lastActiveRow;


$(document).ready(async function() {
    console.log('Parser JS document ready!')

    editor = CodeMirror.fromTextArea(document.getElementById('jquery-code'), {
        mode: "javascript",
        theme: "material",
        lineNumbers: true
    });

    postEditor = new Quill('#postEditor', {
        theme: 'snow'
    });

    table = await createTable({
        table_id: '#example-table',
        selectable: 1,
        columns: [
            {formatter:"rowSelection", titleFormatter:"rowSelection", hozAlign:"center", headerSort:false, width:30},
            {title:"Domen", field:"domen", width:80},
            {title:"Link", field:"link", width:200, formatter:function(cell, formatterParams, onRendered){
                var link = cell.getValue();
                return "<a href='" + link + "' target='_blank'>" + link + "</a>";
            }},
            {title:"Title", field:"title", width:200, editor:'input'},
            {title:"Instruction", field:"instruction", width:150},
            {title:"Instruction id", field:"instruction_id", visible: false},
            {title:"Post id", field:"post_id", visible: false},
            {title:"Telegra Post", field:"telegra_post", width:90,  hozAlign:"center", formatter:"tickCross", sorter:"boolean", editor:true},
            {title:"html_content", field:"html_content", visible: false},
        ],
        data: await getTableData('/api/posts'),
    })

    table.on("rowClick", function(e, row){
        //e - the click event object
        //row - row component
        last_clicked_row = row
        var instruction = row._row.data.instruction
            
        if (instruction !== null) {
            editor.setValue(instruction)
        } else {
            editor.setValue(
`iframeContent.find('.class').each(function() {
    // your parse code here
});`
            )
        }
    });

    table.on("cellEdited", function(cell){
        //cell - cell component
        //console.log(cell._cell.row.data)
        fetch('/parser-update-title', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                'post_id': last_clicked_row._row.data.post_id,
                'title': cell._cell.row.data['title']
            })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error: code ${response.status}`)
            }
            return response.json()
        })
        .then(data => {
            console.log(`Title has been updated! ${data}`)
            refreshTableData('/api/posts')
        })
        .catch(e => {
            alert(`Error while updating title! ${e}`)
        })
    });

    table.on("rowSelected", (row) => {
        lastActiveRow = row.getData();
        console.log("Последняя активная строка:", lastActiveRow);
    })
    // ==============================================================> Buttons cliks
    // =====
    $('#run-jquery').click(function() {
        var html_content = lastActiveRow['html_content'];
        var userCode = editor.getValue()

        console.log("userCode:: " + userCode)
        var result = new Function('context', 'return context.' + userCode)($('<div>').html(html_content));
        console.log(result);

        postEditor.setText(result)
        //insertIntoQuill(quill, content);
    });

    $('#post-telegra').click(function() {
        console.log(JSON.stringify({author: getAuthor(), title: getTitle(), content: content}))
        fetch('/news-editor', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({author: 'author', title: getTitle(), content: content})
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            term.write(`\x1b]8;;${data.url}\x1b\\${data.url}\x1b]8;;\x1b\\\r\n$ `);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
        
    });
    
    $('#save-jquery').click(function() {
        if (!$.isEmptyObject(last_clicked_row)) {
            console.log(last_clicked_row._row.data.instruction)
            console.log(last_clicked_row._row.data)
            try {
                fetch('/update-instruction', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        'post_id': last_clicked_row._row.data.post_id,
                        'instruction_id': last_clicked_row._row.data.instruction_id,
                        'instruction': editor.getValue(),
                    })
                })
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error: code ${response.status}`)
                    }
                    return response.json()
                })
                .then(data => {
                    console.log(data)
                    console.log(`Instruction has been saved! ${data}`)
                    refreshTableData('/api/posts')
                })
                .catch(e => {
                    alert(`Error while updating instruction! ${e}`)
                })
            } catch (error) {
                alert(`parser.js: Some error while updating instuction! ${error}`)
            } 
        } else {
            alert('There is no selected rows!')
        }
    });

    $('#btn-delete').click(() => {
        fetch('/posts-delete', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                'post_id': last_clicked_row._row.data.post_id,
                'instruction_id': last_clicked_row._row.data.instruction_id,
                'instruction': editor.getValue(),
            })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error: code ${response.status}`)
            }
            return response.json()
        })
        .then(data => {
            console.log(data)
            console.log(`Instruction has been saved! ${data}`)
            refreshTableData('/api/posts')
        })
        .catch(e => {
            alert(`Error while updating instruction! ${e}`)
        })
    })

    $('#btn-loadhtml').click(() => {
        var html_content = lastActiveRow['html_content']

        var iframeContent = $('<div>').html(html_content);
        var userCode = $('#jquery-code').val();
        
        try {
            var script = new Function('iframeContent', 'resultArea', userCode);
            script(iframeContent, $('#editor'));
        } catch (e) {
            $('#jquery-result').text('Ошибка выполнения кода: ' + e.message);
        }

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
            $('#btn-delete').text(`Delete`)
        } else {
            $('#btn-delete').text(`Delete (${data.length})`)
        }
    });


    // =====
    // ==============================================================> Table events

    const term = new Terminal();
    //term.open(document.getElementById('terminal'));
    //term.write('Welcome to xterm.js\r\n$ ');

    let input = '';
    // Обработчик для ввода пользователя
    term.onData(e => {
        switch (e) {
            case '\r': // Enter
                term.write('\r\n');
                if (input.startsWith('open ')) {
                    const url = input.slice(5);
                    term.write(`Opening ${url}\r\n`);
                    term.write(`\x1b]8;;${url}\x1b\\Click here to open the link\x1b]8;;\x1b\\\r\n$ `);
                } else {
                    term.write(`You entered: ${input}\r\n$ `);
                }
                input = '';
                break;
            case '\u0003': // Ctrl+C
                term.write('^C\r\n$ ');
                input = '';
                break;
            case '\u007F': // Backspace
                if (input.length > 0) {
                    input = input.slice(0, -1);
                    term.write('\b \b');
                }
                break;
            case '\u001B[3~': // Delete
                // Удаление символов в терминале не так просто реализовать как Backspace, так как это требует изменения содержимого внутри строки
                // Но для простоты, здесь не будет реализовано
                break;
            default:
                if (e >= ' ' && e <= '~') { // Проверка на печатные символы
                    input += e;
                    term.write(e);
                }
                break;
        }
    });


    // Обработчик для ссылок
    term.linkifier.registerLinkMatcher(/https?:\/\/[^\s]+/, (event, uri) => {
        window.open(uri, '_blank');
    });
});