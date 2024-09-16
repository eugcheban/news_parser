// Получаем содержимое iframe
var iframeContent = $('#urlFrame').contents();

var title = '';
var content = [];

function insertIntoQuill(quill, elements) {
    elements.forEach(function(element) {
        if (typeof element === 'string') {
            quill.insertText(quill.getLength() - 1, element);
        } else {
            var format = element.tag;

            // Атрибуты
            var attrs = element.attrs || {};

            switch (format) {
                case 'h3':
                    quill.insertText(quill.getLength() - 1, element.children.join(''), { 'header': 3 });
                    break;
                case 'p':
                    insertIntoQuill(quill, element.children);
                    quill.insertText(quill.getLength() - 1, "\n");
                    // Добавляем пустой абзац для отступа
                    quill.insertText(quill.getLength() - 1, "\n", { 'block': 'paragraph' });
                    break;
                case 'b':
                    quill.insertText(quill.getLength() - 1, element.children.join(''), { 'bold': true });
                    break;
                case 'i':
                    quill.insertText(quill.getLength() - 1, element.children.join(''), { 'italic': true });
                    break;
                case 'a':
                    quill.insertText(quill.getLength() - 1, element.children.join(''), { 'link': attrs.href });
                    break;
                case 'img':
                    quill.insertEmbed(quill.getLength() - 1, 'image', attrs.src);
                    break;
                case 'ul':
                    element.children.forEach(function(child) {
                        if (child.tag === 'li') {
                            quill.insertText(quill.getLength() - 1, child.children.join(''), { 'list': 'bullet' });
                            quill.insertText(quill.getLength() - 1, "\n");
                        }
                    });
                    break;
                default:
                    insertIntoQuill(quill, element.children);
                    quill.insertText(quill.getLength() - 1, "\n");
                    break;
            }
        }
    });
}

// Функция для обработки детей элемента
function processChildren(element) {
    var children = [];
    $(element).contents().each(function() {
        if (this.nodeType === Node.TEXT_NODE) {
            children.push(this.nodeValue);
        } else if (this.nodeType === Node.ELEMENT_NODE) {
            children.push(processElement(this));
        }
    });
    return children;
}

// Функция для обработки элемента
function processElement(element) {
    var obj = { tag: element.tagName.toLowerCase(), children: [] };

    if (element.attributes.length > 0) {
        obj.attrs = {};
        $.each(element.attributes, function() {
            obj.attrs[this.name] = this.value;
        });
    }

    obj.children = processChildren(element);
    return obj;
}

// Функция получения заголовка статьи
function getTitle() {
    return $('#urlFrame').contents()[0].title;
}

// Функция получения выбранного автора статьи
function getAuthor() {
    return $('#authors').val()
}