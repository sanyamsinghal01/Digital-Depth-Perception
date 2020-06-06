#include<Python.h>
#include<limits>
#include<math.h>
#include<algorithm>

static PyObject *exmodError;

static PyObject* exmod_dispmap(PyObject* self,PyObject *args)
{
    int **imgL,**imgR,row_L,col_L,row_R,col_R,row_w,col_w,nbh,step;
    if (!PyArg_ParseTuple(args, "iiiiiiiiii", &imgL, &imgR, &row_L, &col_L, &row_R,&col_R, &row_w, &col_w, &nbh, &step))
    {
        return NULL;
    }
    int *dmap;
    double ssd[2],sum1;
    int a = std::numeric_limits<int>::min();
    for(int i=0;i<row_L;i++)
    {
        for(int j=0;j<col_L-col_w;j++)
        {
            ssd[0]=a;
            ssd[1]=0;
            for(int l=std::max(0,j-nbh);j<std::min(col_L-col_w,j+nbh);l+step)
            {
                sum1=0;
                for(int m=i;m<std::min(i+row_w+1,row_L);m++)
                {
                    for(int n=0;n<col_w+1;n++)
                    {
                        sum1+=pow((imgL[m][j+n]-imgR[m][l+n]),2);
                    }
                }
                if(sum1<ssd[0])
                {
                    ssd[0]=sum1;
                    ssd[1]=abs(l-j);
                }
            }
            dmap[j+(i*col_L)]=ssd[1];
        }
    }
    int max_el=0;
    for(int i=0;i<row_L*(col_L-col_w);i++)
    {
            if(dmap[i]>max_el)
            {
                max_el=dmap[i];
            }
    }
    for(int i=0;i<row_L*(col_L-col_w);i++)
    {
            if(max_el!=0)
            {dmap[i]/=max_el;}
    }
    return Py_BuildValue("o",dmap);
}

static PyMethodDef exmod_methods[]={
    {"dispmap", exmod_dispmap, METH_VARARGS, "Disparity Map"},
    {NULL, NULL, 0, NULL}
};
static struct PyModuleDef exmod =
{
    PyModuleDef_HEAD_INIT,
    "exmod", /* name of module */
    "",          /* module documentation, may be NULL */
    -1,          /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
    exmod_methods
};

PyMODINIT_FUNC PyInit_exmod(void)
{
    return PyModule_Create(&exmod);
}
