chrome.action.onClicked.addListener(function(tab) {
    fetch(chrome.runtime.getURL("free_neetcode_150_list.txt"))
        .then((response) => response.text())
        .then(text => {
            lines = text.toString().split('\n')
            chrome.tabs.create({'url': lines[Math.floor(Math.random() * lines.length)]})
        })
    
	// chrome.tabs.create({'url': 'https://www.google.com'}, function(tab) {
	// 	// Tab opened.
	// });
})
