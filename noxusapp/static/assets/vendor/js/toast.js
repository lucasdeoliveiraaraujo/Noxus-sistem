const toastr = ({theme,icon,title,notificationTime,message}) =>{
    return `
    
      <div class="position-fixed bottom-0 right-0 p-3" style="z-index: 5; right: 0; bottom: 0; position: absolute; top: 0; right: 0;"
>
        <div class="bs-toast toast fade hide bg-${theme}" id="toast" role="alert" aria-live="assertive" aria-atomic="true">
          <div class="toast-header">
            
            <i class='bx bxs-bell-ring' ></i>
            <div class="me-auto fw-semibold">
              ${title}  
            </div>
            ${notificationTime == undefined || notificationTime == null ? "" : "<small> "+notificationTime+"</small>" }
            <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
          </div>
          <div class="toast-body">
            ${message}
          </div>
        </div>
      </div>`
}