$(document).ready(function() {
    console.log('ready asdf;hwqefoihasdf')
    // Define the jQuery code for each version
    const codeVersions = {
        version_1: `find('h1').text();`,
        version_2: "console.log('This is version 2');"
    };

    // Function to update the textarea based on the selected version
    function updateTextarea() {
        const selectedVersion = $('#jquery-variation').val();
        $('#jquery-code').val(codeVersions[selectedVersion]);
    }

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
