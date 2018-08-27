class MathPlot{
    constructor(){
        this.LINE_SIZE = 1;
        this.GRID_SIZE = 25;
        this.canvas = document.getElementById("myCanvas");
        this.canvasCtx = this.canvas.getContext("2d");
        this.drawAxis();
        this.defineOrigin();
    }

    async drawPoint(x, y){
        this.canvasCtx.fillRect(x, y, this.LINE_SIZE, this.LINE_SIZE);
    }

    defineOrigin(){
        let xOrigin = this.canvas.width/2;
        let yOrigin = this.canvas.height/2;
        this.canvasCtx.translate(xOrigin, yOrigin);
        this.canvasCtx.scale(1, -1);
        this.MAX_LENGTH = this.canvas.width;
    }

    async execEquation(callbackEquation, input){
        return callbackEquation(input);
    }

    async draw2DCurve(callbackEquation){
        for(let x = -700; x < this.MAX_LENGTH; x += .1){
            let y = await this.execEquation(callbackEquation, x);
            await this.drawPoint(x, y);
        }
    }

    _drawAxis(ctx, canvasWidth, canvasHeight, numLines, basePos, isX){
        for(let i = 0; i <= numLines; i++) {
            ctx.beginPath();
            ctx.lineWidth = 1;
            ctx.strokeStyle = (i == basePos)? "#000000" : "#e9e9e9";
            
            if(i == numLines) {
                if(isX){
                    ctx.moveTo(0, this.GRID_SIZE*i);
                    ctx.lineTo(canvasWidth, this.GRID_SIZE*i);
                }else{
                    ctx.moveTo(this.GRID_SIZE*i, 0);
                    ctx.lineTo(this.GRID_SIZE*i, canvasHeight);
                }
            } else {
                if(isX){
                    ctx.moveTo(0, this.GRID_SIZE*i);
                    ctx.lineTo(canvasWidth, this.GRID_SIZE*i);
                }else{
                    ctx.moveTo(this.GRID_SIZE*i+0.5, 0);
                    ctx.lineTo(this.GRID_SIZE*i+0.5, canvasHeight);
                }
            }

            ctx.stroke();
        }
    }

    drawAxis(){
        let canvasWidth = this.canvas.width;
        let canvasHeight = this.canvas.height;
        let numLines = Math.floor(canvasHeight/this.GRID_SIZE);
        let baseXposition = numLines/2;

        this._drawAxis(this.canvasCtx, canvasWidth, canvasHeight, numLines, baseXposition, true);
        this._drawAxis(this.canvasCtx, canvasWidth, canvasHeight, numLines, baseXposition);
    }
}

mathPlot = new MathPlot();
mathPlot.draw2DCurve(x => x**2/200);