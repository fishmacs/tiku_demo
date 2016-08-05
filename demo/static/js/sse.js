function queryConvertState(docs) {
  var docIds = JSON.parse(docs);
  var es = new EventSource("/sse/query/convert");
  
  es.onerror = function(err) {
    console.log(err);
    es.close();
  };
  
  es.onmessage = function(event) {
    console.log(event.data);
    stillConverting = JSON.parse(event.data);
    var reload = false;
    for (var i=0; i < docIds.length;) {
      var docId = docIds[i];
      if (stillConverting.indexOf(docId) >= 0) {
        i++;
      } else {
        docIds.splice(i, 1);        
        $('#convert_state_' + docId).text('转换完成');
        $('#converting_' + docId).remove();
        // reload = true;
        break;
      }
    }
    // if (!docIds.length)
    //   es.close();
    if(reload) {
      es.close();
      setTimeout(function() { window.location.reload(); }, 1000);
    }
  };
}

function queryExportState(exams) {
  var examIds = JSON.parse(exams);
  var es = new EventSource("/sse/query/export");
  
  es.onerror = function(err) {
    console.log(err);
    es.close();
  };
  
  es.onmessage = function(event) {
    console.log(event.data);
    working = JSON.parse(event.data);
    var reload = false;
    for (var i=0; i < examIds.length;) {
      var id = examIds[i];
      if (working.indexOf(id) >= 0) {
        i++;
      } else {
        examIds.splice(i, 1);        
        $('#export_state_' + id).text('转换完成');
        $('#exporting_' + id).remove();
        $('#download_' + id).show();
        // reload = true;
        break;
      }
    }
    // if (!examIds.length)
    //   es.close();
    if(reload) {
      es.close();
      setTimeout(function() { window.location.reload(); }, 1000);
    }
  };
}
