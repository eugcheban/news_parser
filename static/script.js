import {
    updateTextarea,
} from './utils.js'

$(document).ready(function() {
    // Event listener for the select change
    $('#jquery-variation').change(function() {
        updateTextarea();
    });

    // Event listener for the Previous button
    $('#previous').click(function() {
        let currentIndex = $('#jquery-variation option:selected').index();
        if (currentIndex > 0) {
            currentIndex--;
            $('#jquery-variation').prop('selectedIndex', currentIndex);
            updateTextarea();
        }
    });

    // Event listener for the Next button
    $('#next').click(function() {
        let currentIndex = $('#jquery-variation option:selected').index();
        const optionsLength = $('#jquery-variation option').length;
        if (currentIndex < optionsLength - 1) {
            currentIndex++;
            $('#jquery-variation').prop('selectedIndex', currentIndex);
            updateTextarea();
        }
    });

    // Initialize the textarea with the first version code
    updateTextarea();
});
