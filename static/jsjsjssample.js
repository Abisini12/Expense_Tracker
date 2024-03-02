function toggleContainer() {
    var container =  document.querySelector('.container-add');
    var full_container= document.querySelector('.budget_tacker_info');
    var button1=document.getElementById('add_product');
    var button2=document.getElementById('save_product');
    var table= document.querySelector('.product_table_and_result');
    if (container.style.display === 'none' || container.style.display === '') {
      container.style.display = 'block';
      full_container.style.display='none';
      button1.style.display='none';
      button2.style.display='none';
      table.style.display='none';
      // document.body.style.backgroundColor = 'rgba(192, 192, 192, 0.637)';
      // document.body.style.background='rgba(128, 128, 128, 0.5)';
      // document.body.style.filter='brightness(30%)'
      
    } else {
      container.style.display = 'none';
      container = null;
      full_container.style.display='grid';
      button1.style.display='grid';
      button2.style.display='grid';
      table.style.display='grid';
      // document.body.style.background='fff189';
      document.body.style.filter = ''; // removes the filter
    }
  }
  
var error=document.getElementById('warning');
var remaining=document.getElementById('remaining_value');
if(remaining<0)
{
  error.style.display='none';
}
else { error.style.display='grid'}

