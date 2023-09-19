chrome.runtime.onMessage.addListener(function (message, sender, sendResponse) {
    if (message.createNewTab) {
      // Create a new tab with the desired URL.
      chrome.tabs.create({ url: "https://google.com" }); // Replace with your desired URL.
    }
  });
  