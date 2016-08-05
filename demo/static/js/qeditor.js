MathJax.Hub.Config({
  jax: ["input/MathML", "input/AsciiMath", "output/NativeMML"],
  extensions: ["asciimath2jax.js","mml2jax.js","MathMenu.js","MathZoom.js","MathEvents.js","toMathML.js"],
  // Apparently we can't change the escape sequence for ASCIIMath (MathJax doesn't find it)
  // asciimath2jax: { inlineMath: [["[ASCIIMATH_START]", "[ASCIIMATH_END]"]], },
  AsciiMath: { noErrors: { disabled: true } }
});

var buttons;

Aloha.ready(function(){
  Aloha.require(['genericbutton/genericbutton-plugin'], function(GenericButton){
    // Save button is disabled until something is changed
    buttons = GenericButton.getButtons();
    buttons.save.enable(false);

    //var body_url = '/qeditor/QEditor/sandbox/index.html';

    // Fetch MML content
    Aloha.jQuery.get(env.loadUrl, function(data) {
      var $d = Aloha.jQuery('<div />').html(data);
      var $editable = Aloha.jQuery('#canvas').html(
        $d.find('> *'));

      // Remove the pyramid debug toolbar from the preview
      // if it exists. This code should do nothing in production
      $editable.find('#pDebug').remove();
      $editable.aloha().focus();

      MathJax.Hub.Configured();

      setInterval(function() {
        var editor = Aloha.getEditableById('canvas');
        if (editor.isModified()) {
          $('.btn.save').html('保存');
          GenericButton.getButtons().save.enable(true);
        }
      }, 250);
    });
  });
});

function saveMML(){
  var editor = Aloha.getEditableById('canvas');
  if(editor.isModified()){
    var content = editor.getContents();
    if(env.saveUrl !== null){
      $.post(
        env.saveUrl,
        {content: content},
        function(data, statustext){
          if(data.error){
            alert('保存失败' + data.error);
          } else {
            buttons.save.enable(false);
          }
        });
    }
  }
}
