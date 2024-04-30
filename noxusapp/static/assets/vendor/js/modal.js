const Modal = ({...props}) =>{
    return `
    <div className="modal fade show" id="mdl${props.id}" tabIndex="-1" style="display: none;" aria-modal="true" role="dialog">
        <div className="modal-dialog modal-sm" role="document">
            <div className="modal-content">
                <div className="modal-header">
                    <h5 className="modal-title">${props.titulo}</h5>
                    <button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div className="modal-body">
                    ${props.corpo.join("")}
                </div>
                <div className="modal-footer">
                    ${props.rodape.join("")}
                </div>
            </div>
        </div>
    </div>`
}