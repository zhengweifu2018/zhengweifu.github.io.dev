// IgniteRayPick.cs

using UnityEngine;
using System.Collections;
using UnityEngine.UI;

namespace Ignite
{
    public struct PointerEventArgs
    {
        public uint controllerIndex;
        public uint flags;
        public float distance;
        public Transform target;
    }

    public delegate void PointerEventHandler(object sender, PointerEventArgs e);
    public class IgniteRayPick : MonoBehaviour
    {
        public bool active = true;
        public Color color;
        public float thickness = 0.001f;
        public GameObject holder;
        public GameObject pointer;
        bool isActive = false;
        public bool addRigidBody = false;
        public Transform reference;
        public event PointerEventHandler PointerIn;
        public event PointerEventHandler PointerOut;

        Transform previousContact = null;

        private GameObject colliderObject;


        //射线拾取高亮
        public Material highMat;
        private Material preMat1, preMat2, preMat3, preMat4;
        // Use this for initialization
        void Start()
        {
            colliderObject = null;

            holder = new GameObject();
            holder.transform.parent = this.transform;
            holder.transform.localPosition = Vector3.zero;

            pointer = GameObject.CreatePrimitive(PrimitiveType.Cube);
            pointer.transform.parent = holder.transform;
            pointer.transform.localScale = new Vector3(thickness, thickness, 100f);
            pointer.transform.localPosition = new Vector3(0f, 0f, -50.001f);
            BoxCollider collider = pointer.GetComponent<BoxCollider>();
            if (addRigidBody)
            {
                if (collider)
                {
                    collider.isTrigger = true;
                }
                Rigidbody rigidBody = pointer.AddComponent<Rigidbody>();
                rigidBody.isKinematic = true;
            }
            else
            {
                if (collider)
                {
                    Object.Destroy(collider);
                }
            }
            Material newMaterial = new Material(Shader.Find("Unlit/Color"));
			newMaterial.SetColor("_Color", Color.blue);
            pointer.GetComponent<MeshRenderer>().material = newMaterial;
        }

        public GameObject GetColliderObject()
        {
            return colliderObject;
        }

        public virtual void OnPointerIn(PointerEventArgs e)
        {
            if (PointerIn != null)
                PointerIn(this, e);
            if (e.target.tag == "pick1")
            {
                preMat1 = e.target.GetComponent<Renderer>().material;
                e.target.GetComponent<Renderer>().material = highMat;               
            }
            else if (e.target.tag == "pick2")
            {
                preMat2 = e.target.GetComponent<Renderer>().material;
                e.target.GetComponent<Renderer>().material = highMat;               
            }
            else if (e.target.tag == "pick3")
            {
                preMat3 = e.target.GetComponent<Renderer>().material;
                e.target.GetComponent<Renderer>().material = highMat;               
            }
            else if (e.target.tag == "pick4")
            {
                preMat4 = e.target.GetComponent<Renderer>().material;
                e.target.GetComponent<Renderer>().material = highMat;               
            }
            else if(e.target.tag == "btncart" || e.target.tag == "btnbuy")
            {
				Color color = Color.green;
                //color.a = 0.8f;
                e.target.GetComponent<Image>().color = color;               
            }
        }

        public virtual void OnPointerOut(PointerEventArgs e)
        {
            if (e.target.tag == "pick1")
            {
                e.target.GetComponent<Renderer>().material = preMat1;
            }
            else if (e.target.tag == "pick2")
            {
                e.target.GetComponent<Renderer>().material = preMat2;
            }
            else if (e.target.tag == "pick3")
            {
                e.target.GetComponent<Renderer>().material = preMat3;
            }
            else if (e.target.tag == "pick4")
            {
                e.target.GetComponent<Renderer>().material = preMat4;
            }
            else if (e.target.tag == "btncart" || e.target.tag == "btnbuy")
            {
                Color color = Color.white;
                //color.a = 1.0f;
                e.target.GetComponent<Image>().color = color;
            }

            if (PointerOut != null)
                PointerOut(this, e);
        }

        public void showRay(bool show)
        {
            pointer.SetActive(show);
        }

        // Update is called once per frame
        void Update()
        {
            if (!isActive)
            {
                isActive = true;
                this.transform.GetChild(0).gameObject.SetActive(true);
            }

            float dist = 100f;

            SteamVR_TrackedController controller = GetComponent<SteamVR_TrackedController>();

            Ray raycast = new Ray(transform.position, transform.forward);
            RaycastHit hit;
            bool bHit = Physics.Raycast(raycast, out hit);

           if (previousContact && previousContact != hit.transform)
            {
                PointerEventArgs args = new PointerEventArgs();
                if (controller != null)
                {
                    args.controllerIndex = controller.controllerIndex;
                }
                args.distance = 0f;
                args.flags = 0;
                args.target = previousContact;
                OnPointerOut(args);
                //previousContact = null;
            }

            if (bHit && previousContact != hit.transform)
            {
                PointerEventArgs argsIn = new PointerEventArgs();
                if (controller != null)
                {
                    argsIn.controllerIndex = controller.controllerIndex;
                }

                argsIn.distance = hit.distance;
                argsIn.flags = 0;
                argsIn.target = hit.transform;
                colliderObject = hit.transform.gameObject;
                OnPointerIn(argsIn);
                previousContact = hit.transform;
            }


            if (!bHit)
            {
                previousContact = null;
                colliderObject = null;
            }

            if (bHit && hit.distance < 100f)
            {
                dist = hit.distance;
            }

            if (controller != null && controller.triggerPressed)
            {
                pointer.transform.localScale = new Vector3(thickness * 5f, thickness * 5f, dist);
            }
            else
            {
                pointer.transform.localScale = new Vector3(thickness, thickness, dist);
            }

            pointer.transform.localPosition = new Vector3(0f, 0f, -dist / 2f);
            
        }
    }
}


// IgniteRightLogic

using UnityEngine;
using System.Collections;
using System;
using System.Text;
using System.Security.Cryptography;
using System.IO;
namespace Ignite
{
    public class IgniteRightLogic : MonoBehaviour
    {
        public IgniteUI   mIgniteUI;
        public IgniteWandInteract mInteract;
        public Transform  mJewelryPos; //首饰在手柄上的位置
        public Transform  mCartPos;    //购物车的位置
        public GameObject prefab1, prefab2, prefab3, prefab4;//首饰预设
        private GameObject mJewelry1, mJewelry2, mJewelry3, mJewelry4;//首饰的实例化对象

        int Release = 1;
        private GameObject colliderObj;  //射线碰撞到的物体
        private GameObject grabObject;   //抓住的物体
        SteamVR_TrackedObject mTrackedObj;
        private IgniteRayPick mIgniteRayPick;

        private ArrayList buyList;
        private string buydata;

        private int movetoCartIndex = 0;
        void Start()
        {
            colliderObj = null;
            mIgniteRayPick = GetComponent<IgniteRayPick>();
            mIgniteRayPick.PointerIn  += Ray_PointerIn;
            mIgniteRayPick.PointerOut += Ray_PointerOut;

            mTrackedObj = GetComponent<SteamVR_TrackedObject>();
            buyList = new ArrayList();


        }
        private void Ray_PointerOut(object sender, PointerEventArgs e)
        {
           
        }

        private void Ray_PointerIn(object sender, PointerEventArgs e)
        {
            colliderObj = mIgniteRayPick.GetColliderObject();
            if (colliderObj != null)
            {
               // Debug.Log(colliderObj.name);
            }

        }

        void Update()
        {
            var device = SteamVR_Controller.Input((int)mTrackedObj.index);

            colliderObj = mIgniteRayPick.GetColliderObject();
            if (colliderObj != null && device.GetTouchDown(SteamVR_Controller.ButtonMask.Trigger))
            {
               
                if (colliderObj.tag == "pick1")
                {
                    //如果其他的存先销毁
                    if (mJewelry2 != null) Destroy(mJewelry2);
                    if (mJewelry3 != null) Destroy(mJewelry3);
                    if (mJewelry4 != null) Destroy(mJewelry4);

                    //实例化选中的
                    if (mJewelry1 == null)                    
                       mJewelry1 = GameObject.Instantiate(prefab1);   
                                       
                    grabObject = mJewelry1;
                    grabObject.transform.SetParent(mJewelryPos);
                    //grabObject.transform.position = mJewelryPos.position + offset;
                    //grabObject.transform.position = new Vector3(-0.0f, 0.0f, 0.0f);
                    //grabObject.transform.rotation = Quaternion.Euler(-60.0f, 180.0f, 0.0f);

                    mIgniteUI.setJewelry(1);
                }
                else if(colliderObj.tag == "pick2")
                {
                    //如果其他的存先销毁
                    if (mJewelry1 != null) Destroy(mJewelry1);
                    if (mJewelry3 != null) Destroy(mJewelry3);
                    if (mJewelry4 != null) Destroy(mJewelry4);

                    //实例化选中的
                    if (mJewelry2 == null)
                        mJewelry2 = GameObject.Instantiate(prefab2);
                    grabObject = mJewelry2;
                    grabObject.transform.SetParent(mJewelryPos);
                   // grabObject.transform.position = mJewelryPos.position;
                    //grabObject.transform.rotation = mJewelryPos.rotation;

                    mIgniteUI.setJewelry(2);
                }
                else if (colliderObj.tag == "pick3")
                {
                    //如果其他的存先销毁
                    if (mJewelry1 != null) Destroy(mJewelry1);
                    if (mJewelry2 != null) Destroy(mJewelry2);
                    if (mJewelry4 != null) Destroy(mJewelry4);

                    //实例化选中的
                    if (mJewelry3 == null)
                        mJewelry3 = GameObject.Instantiate(prefab3);
                    grabObject = mJewelry3;
                    grabObject.transform.SetParent(mJewelryPos);
                    // grabObject.transform.position = mJewelryPos.position;

                    mIgniteUI.setJewelry(3);
                }
                else if (colliderObj.tag == "pick4")
                {
                    //如果其他的存先销毁
                    if (mJewelry1 != null) Destroy(mJewelry1);
                    if (mJewelry2 != null) Destroy(mJewelry2);
                    if (mJewelry3 != null) Destroy(mJewelry3);                 

                    //实例化选中的
                    if (mJewelry4 == null)
                        mJewelry4 = GameObject.Instantiate(prefab4);
                    grabObject = mJewelry4;
                    grabObject.transform.SetParent(mJewelryPos);
                    // grabObject.transform.position = mJewelryPos.position;

                    mIgniteUI.setJewelry(4);
                }
                else if (colliderObj.tag == "btncart")
                {
                    addtoCart();
                    //Debug.Log("btncart");
                }
                else if (colliderObj.tag == "btnbuy")
                {
                    buy();
                    //Debug.Log("btnbuy");
                }
            }

            //手柄触碰
            if (Release == 1 && grabObject == null && device.GetTouchDown(SteamVR_Controller.ButtonMask.Trigger) && mInteract.getTouchedObject())
            {
               Debug.Log("grabObject == null && device.GetTouchDown(SteamVR_Controller.ButtonMask.Trigger)");
                GameObject touched = mInteract.getTouchedObject();
             
                if (touched == mJewelry1 && mJewelry1)
                {
                    mIgniteUI.setJewelry(1);
                    grabObject = mJewelry1;
                    grabObject.transform.SetParent(mJewelryPos);
                    //grabObject.transform.position = mJewelryPos.position;
                   // grabObject.transform.localPosition = new Vector3(0.0f, 0.00f, 0.0f);
                   // grabObject.transform.localRotation = Quaternion.Euler(-180.0f, -180.0f, 0.0f);
                }
                else if (touched == mJewelry2 && mJewelry2)
                {
                    mIgniteUI.setJewelry(2);
                    grabObject = mJewelry2;
                    grabObject.transform.SetParent(mJewelryPos);                    
                    // grabObject.transform.position = mJewelryPos.position;
                    //grabObject.transform.localPosition = new Vector3(0.0f, 0.00f, 0.0f);
                    //grabObject.transform.localRotation = Quaternion.Euler(90.0f, 0.0f, 0.0f);
                }
                else if (touched == mJewelry3 && mJewelry3)
                {
                    mIgniteUI.setJewelry(3);
                    grabObject = mJewelry3;
                    grabObject.transform.SetParent(mJewelryPos);
                    //grabObject.transform.position = mJewelryPos.position;
                    //grabObject.transform.localPosition = new Vector3(0.0f, 0.0f, 0.0f);
                    //grabObject.transform.localRotation = Quaternion.Euler(90.0f, 0.0f, 0.0f);
                }
                else if (touched == mJewelry4 && mJewelry4)
                {
                    mIgniteUI.setJewelry(4);
                    grabObject = mJewelry4;
                    grabObject.transform.SetParent(mJewelryPos);
                    //grabObject.transform.position = mJewelryPos.position;
                   // grabObject.transform.localPosition = new Vector3(0.0f, 0.00f, 0.0f);
                    //grabObject.transform.localRotation = Quaternion.Euler(90.0f, 0.0f, 0.0f);
                }
     
            }

            if (grabObject != null && device.GetTouchDown(SteamVR_Controller.ButtonMask.Trigger))
            {
                Vector3 offset = new Vector3(0.0f,0.05f, 0.15f);
                grabObject.transform.SetParent(mJewelryPos);
                grabObject.transform.localPosition = offset;               
                grabObject.transform.localRotation = Quaternion.Euler(-40.0f, 180.0f, 0.0f);
                if(grabObject == mJewelry2 || grabObject == mJewelry3|| grabObject == mJewelry4)
                {
                    grabObject.transform.localScale = new Vector3(4.0f, 4.0f, 4.0f);
                } else if(grabObject == mJewelry1) {
                    grabObject.transform.localScale = new Vector3(2.0f, 2.0f, 2.0f);
                }
                
                Release = 0;

                mIgniteRayPick.showRay(false);
            }
            else if (grabObject != null && device.GetTouchUp(SteamVR_Controller.ButtonMask.Trigger))
            {
                grabObject.transform.SetParent(null);
                //grabObject.transform.position = mJewelryPos.position;
                grabObject = null;
                Release = 1;
                mIgniteRayPick.showRay(true);
            }
        }

        void addtoCart()
        {
            if (mJewelry1 &&  1== mIgniteUI.getJewlryIndex())
            {
                Debug.Log(1111111);
                movetoCartIndex = 1;           
                if (!IsInvoking("JewelryMovetoCart"))
                     InvokeRepeating("JewelryMovetoCart", 0, 0.01F);
            }
            if (mJewelry2 && 2 == mIgniteUI.getJewlryIndex())
            {
                movetoCartIndex = 2;
                if (!IsInvoking("JewelryMovetoCart"))
                    InvokeRepeating("JewelryMovetoCart", 0, 0.01F);
            }
            if (mJewelry3 && 3 == mIgniteUI.getJewlryIndex())
            {
                movetoCartIndex = 3;
                if (!IsInvoking("JewelryMovetoCart"))
                    InvokeRepeating("JewelryMovetoCart", 0, 0.01F);
            }
            if (mJewelry4 && 4 == mIgniteUI.getJewlryIndex())
            {
                movetoCartIndex = 4;
                if (!IsInvoking("JewelryMovetoCart"))
                    InvokeRepeating("JewelryMovetoCart", 0, 0.01F);
            }
           

        }

        void buy()
        {
             if (buyList.Count == 0) return;
            mIgniteUI.setJewelry(0);
            buyList.Sort();
           
            int buyindex1 = 0, buyindex2 = 0, buyindex3 = 0, buyindex4 = 0;
            foreach (int i in buyList)
            {
                if(i==1) buyindex1++;
                else if(i==2) buyindex2++;
                else if (i == 3) buyindex3++;
                else if (i == 4) buyindex4++;
            }
            buyList.Clear();
            buydata = "{\"detail\":\"";
            if (buyindex1 > 0) buydata += ("28066:" + buyindex1.ToString());
            if (buyindex2 > 0)
            {   if (buyindex1 > 0) buydata += ",";
                buydata += ("39243:" + buyindex2.ToString());
            }
            if (buyindex3 > 0)
            {
                if (buyindex1 > 0 || buyindex2>0) buydata += ",";
                buydata += ("37365:" + buyindex3.ToString());
            }
            if (buyindex4 > 0)
            {
                if (buyindex1 > 0 || buyindex2 > 0 || buyindex3 > 0) buydata += ",";
                buydata += ("39242:" + buyindex4.ToString());
            }
            buydata += "\"}";
            
            
            StartCoroutine(TestPost());
        }

        void JewelryMovetoCart()
        {
            if(movetoCartIndex == 1)
            {
                mJewelry1.transform.position = Vector3.Lerp(mJewelry1.transform.position, mCartPos.position,Time.deltaTime * 1.0f);
                if (Vector3.Distance(mJewelry1.transform.position , mCartPos.position)<0.1f)
                {
                    mIgniteUI.setJewelry(0);
                    Destroy(mJewelry1);
                    mJewelry1 = null;
                    grabObject = null;
                    buyList.Add(1);
                    movetoCartIndex = 0;
                    CancelInvoke("JewelryMovetoCart");                    
                }
            }
            else if (movetoCartIndex == 2)
            {
                mJewelry2.transform.position = Vector3.Lerp(mJewelry2.transform.position, mCartPos.position, Time.deltaTime * 1.0f);
                if (Vector3.Distance(mJewelry2.transform.position, mCartPos.position) < 0.1f)
                {
                    mIgniteUI.setJewelry(0);
                    Destroy(mJewelry2);
                    mJewelry2 = null;
                    grabObject = null;
                    buyList.Add(2);
                    movetoCartIndex = 0;
                    CancelInvoke("JewelryMovetoCart");
                }
            }
            else if (movetoCartIndex == 3)
            {
                mJewelry3.transform.position = Vector3.Lerp(mJewelry3.transform.position, mCartPos.position, Time.deltaTime * 1.0f);
                if (Vector3.Distance(mJewelry3.transform.position, mCartPos.position) < 0.1f)
                {
                    mIgniteUI.setJewelry(0);
                    Destroy(mJewelry3);
                    mJewelry3 = null;
                    grabObject = null;
                    buyList.Add(3);
                    movetoCartIndex = 0;
                    CancelInvoke("JewelryMovetoCart");
                }
            }
            else if (movetoCartIndex == 4)
            {
                mJewelry4.transform.position = Vector3.Lerp(mJewelry4.transform.position, mCartPos.position, Time.deltaTime * 1.0f);
                if (Vector3.Distance(mJewelry4.transform.position, mCartPos.position) < 0.1f)
                {
                    mIgniteUI.setJewelry(0);
                    Destroy(mJewelry4);
                    mJewelry4 = null;
                    grabObject = null;
                    buyList.Add(4);
                    movetoCartIndex = 0;
                    CancelInvoke("JewelryMovetoCart");
                }
            }

        }

        //把数据提交到网页
        IEnumerator TestPost()
        {
            //WWW的三个参数: url, postData, headers  
            string url = "http://www.ignjewelry.com/api.php/services/rest";

            WWWForm newForm = new WWWForm();
            newForm.AddField("method", "front.vrcartorder");

            string visa = Convert.ToBase64String(Encoding.Default.GetBytes("vr@ign.vip 123456"));
            visa = "dnJAaWduLnZpcCAxMjM0NTY="; //演示用
            newForm.AddField("visa", visa);

            newForm.AddField("format", "json");

            System.Random rand = new System.Random();
            int vcode = rand.Next(1, 28);
            vcode = 10;//演示用
            newForm.AddField("vcode", vcode.ToString()); //1-28的随机数

            string curlPost = "method=front.vrcartorder&visa=" + visa + "&format=json";
            string pubKey = "O4rDRqwshSBojonvTt4mar21Yv1Ehmqm";
            //string sign = gensign(curlPost, vcode, pubKey);
            string sign = "9e5cf4532551b8be30e3955eef8d9683";//演示用
            newForm.AddField("sign", sign);

            newForm.AddField("debug", "0");

            //string dataArr = "{detail:39242:1,28066:1,37365:1,39243:1}";
            //string dataArr = "{\"detail\":\"28066:1,37365:1,39243:1\"}";

            //Debug.Log(dataArr);
            string dataArr = Convert.ToBase64String(Encoding.Default.GetBytes(buydata));
           // dataArr = "eyJkZXRhaWwiOiIzOTI0MjoxLDI4MDY2OjEsMzczNjU6MSwzOTI0MzoxIn0=";
             
            newForm.AddField("datas", dataArr);


            //发送请求  
            WWW www_instance = new WWW(url, newForm);

            //web服务器返回  
            yield return www_instance;
            if (www_instance.error != null)
            {
                Debug.Log(www_instance.error);
            }
            else
            {
                Debug.Log(www_instance.text);
            }
        }



    }
}

// IgniteScreenVideo

using UnityEngine;
using System.Collections;

public class IgniteScreenVideo : MonoBehaviour {

    public MovieTexture movTexture;

    // Use this for initialization
    void Start () {
        GetComponent<Renderer>().material.mainTexture = movTexture;
        movTexture.Play();
        movTexture.loop = true;
    }
}

// IgniteUI

using UnityEngine;
using System.Collections;
using UnityEngine.UI;
namespace Ignite
{
    public class IgniteUI : MonoBehaviour
    {
        public Transform             mUIPos;    //UI挂接位置
        public GameObject            mUIRoot;   //UI根对象
        public SteamVR_TrackedObject mTrackedObj;

        //UI 对象
        public Image    canvasImg; //详细信息图片
        public Image    canvasImgDy; //动态信息图片
        public RawImage canvasMV;   //试戴视频

        public MovieTexture movieTex1, movieTex2, movieTex3, movieTex4; //试戴视频资源
        public Sprite imageTex1, imageTex2, imageTex3, imageTex4;       //详细信息资源       
        //动态图片信息
        public Sprite dyImg11, dyImg12, dyImg13;
        public Sprite dyImg21, dyImg22, dyImg23;
        public Sprite dyImg31, dyImg32, dyImg33;
        public Sprite dyImg41, dyImg42, dyImg43;

        private int mIndex = 0;
        private int mDyIndex = 0;
        bool IsShock = false;
        
        
        float mRotateUI = 0;

        bool mTracking = false;
        bool mCheckTrack = false;
        // The angle range for detecting swipe
        private const float mAngleRange = 30;
        // To recognize as swipe user should at lease swipe for this many pixels
        private const float mMinSwipeDist = 0.2f;
        private const float mMinVelocity = 4.0f;
        private readonly Vector2 mXAxis = new Vector2(1, 0);
        private readonly Vector2 mYAxis = new Vector2(0, 1);
        private Vector2 mStartPosition;
        private Vector2 mEndPosition;
        private float mSwipeStartTime;
        void Start()
        {
            mUIRoot.transform.parent = mUIPos;

            mUIRoot.transform.localPosition = new Vector3(0.0f, 0.00f, 0.1f);
            mUIRoot.transform.localRotation = Quaternion.Euler(90.0f, 0.0f, 0.0f);
            mUIRoot.SetActive(false);     
        }
  
        void FixedUpdate()
        {
            var device = SteamVR_Controller.Input((int)mTrackedObj.index);
            if (device.GetPressDown(SteamVR_Controller.ButtonMask.Trigger))
            {
                mUIRoot.SetActive(true);
               
            }

            if ((int)mTrackedObj.index != -1 && device.GetTouchDown(Valve.VR.EVRButtonId.k_EButton_Axis0))
            {
                mTracking = true;
                mStartPosition = new Vector2(device.GetAxis(Valve.VR.EVRButtonId.k_EButton_Axis0).x, device.GetAxis(Valve.VR.EVRButtonId.k_EButton_Axis0).y);
                mSwipeStartTime = Time.time;
                Debug.Log("touch in");
            }
            else if (device.GetTouchUp(Valve.VR.EVRButtonId.k_EButton_Axis0))
             {                 
                //mTracking = false;
                mCheckTrack = true;
                Debug.Log("touch out");
            }
            else if (mTracking)
            {
                mEndPosition = new Vector2(device.GetAxis(Valve.VR.EVRButtonId.k_EButton_Axis0).x,device.GetAxis(Valve.VR.EVRButtonId.k_EButton_Axis0).y);
            }

            if(mCheckTrack)
            {
                mCheckTrack = false;
                float deltaTime = Time.time - mSwipeStartTime;
                Vector2 swipeVector = mEndPosition - mStartPosition;
                float velocity = swipeVector.magnitude / deltaTime;
                
                if (velocity > mMinVelocity && swipeVector.magnitude > mMinSwipeDist)
                {
                    float angleOfSwipe = Vector2.Dot(swipeVector, mXAxis);
                    Debug.Log(angleOfSwipe);
                    //angleOfSwipe = Mathf.Acos(angleOfSwipe) * Mathf.Rad2Deg;
                    
                    // Detect left and right swipe
                    if (angleOfSwipe < 0)
                    {
                        mRotateUI = -2;
                        IsShock = false;  //每次按下，IsShock为false,才能保证手柄震动
                         StartCoroutine("Shock", 0.1f); //开启协程Shock(),第二个参数0.5f 即为协程Shock()的形参
                    }
                    else if (angleOfSwipe>0)
                    {
                        mRotateUI = 2;
                        IsShock = false;  //每次按下，IsShock为false,才能保证手柄震动
                        StartCoroutine("Shock", 0.1f); //开启协程Shock(),第二个参数0.5f 即为协程Shock()的形参
                    }
                    else {
                       // angleOfSwipe = Vector2.Dot(swipeVector, mYAxis);
                       // angleOfSwipe = Mathf.Acos(angleOfSwipe) * Mathf.Rad2Deg;
                    }
                }

            }
            


            if (device.GetPressDown(SteamVR_Controller.ButtonMask.Touchpad))
            {
                Vector2 point = device.GetAxis();
                if(point.x<0)
                {
                    mRotateUI = -2;
                    IsShock = false;  //每次按下，IsShock为false,才能保证手柄震动
                    StartCoroutine("Shock", 0.1f); //开启协程Shock(),第二个参数0.5f 即为协程Shock()的形参
                }
                else
                {
                    mRotateUI = 2;
                    IsShock = false;  //每次按下，IsShock为false,才能保证手柄震动
                    StartCoroutine("Shock", 0.1f); //开启协程Shock(),第二个参数0.5f 即为协程Shock()的形参
                }
            }
            rotateUI();

        }
        public int getJewlryIndex()
        {
            return mIndex;
        }
        public void setJewelry(int index)
        {
            if(mIndex == index) return;
            mIndex = index;
            if (movieTex1.isPlaying) movieTex1.Stop();
            if (movieTex2.isPlaying) movieTex2.Stop();
            if (movieTex3.isPlaying) movieTex3.Stop();
            if (movieTex4.isPlaying) movieTex4.Stop();
            if (index == 0)
            {
                if (IsInvoking("setDynamicImg")) CancelInvoke("setDynamicImg");                
                mUIRoot.SetActive(false);
                Debug.Log("mUIRoot.SetActive(false)");
            }
            if (index == 1)
            {               
                mUIRoot.SetActive(true);
                mUIRoot.transform.localRotation = Quaternion.Euler(90.0f, 0.0f, 0.0f);
                canvasImg.sprite = imageTex1;
                canvasMV.texture = movieTex1;
                movieTex1.wrapMode = TextureWrapMode.Repeat;
                movieTex1.loop = true;
                movieTex1.Play();

                mDyIndex = 0;
                if (IsInvoking("setDynamicImg")) CancelInvoke("setDynamicImg");
                InvokeRepeating("setDynamicImg", 0, 0.9F);

                //每次按下，IsShock为false,才能保证手柄震动               
                if ((int)mTrackedObj.index != -1)
                {
                    IsShock = false;
                    StartCoroutine("Shock", 0.1f);
                }
            }
            else if (index == 2)
            {
                mUIRoot.SetActive(true);
                mUIRoot.transform.localRotation = Quaternion.Euler(90.0f, 0.0f, 0.0f);
                canvasImg.sprite = imageTex2;
                canvasMV.texture = movieTex2;
                movieTex2.wrapMode = TextureWrapMode.Repeat;
                movieTex2.loop = true;
                movieTex2.Play();
                mDyIndex = 0;
                if (IsInvoking("setDynamicImg")) CancelInvoke("setDynamicImg");
                InvokeRepeating("setDynamicImg", 0, 0.9F);

                //每次按下，IsShock为false,才能保证手柄震动
                if ((int)mTrackedObj.index != -1)
                {
                    IsShock = false;
                    StartCoroutine("Shock", 0.1f);
                }
                
            }
            else if (index == 3)
            {
                mUIRoot.SetActive(true);
                mUIRoot.transform.localRotation = Quaternion.Euler(90.0f, 0.0f, 0.0f);
                canvasImg.sprite = imageTex3;
                canvasMV.texture = movieTex3;
                movieTex3.wrapMode = TextureWrapMode.Repeat;
                movieTex3.loop = true;
                movieTex3.Play();
                mDyIndex = 0;
                if (IsInvoking("setDynamicImg")) CancelInvoke("setDynamicImg");
                InvokeRepeating("setDynamicImg", 0, 0.9F);

                //每次按下，IsShock为false,才能保证手柄震动
                if ((int)mTrackedObj.index != -1)
                 {
                    IsShock = false;
                    StartCoroutine("Shock", 0.1f);
                }

            }
            else if (index == 4)
            {
                mUIRoot.SetActive(true);
                mUIRoot.transform.localRotation = Quaternion.Euler(90.0f, 0.0f, 0.0f);
                canvasImg.sprite = imageTex4;
                canvasMV.texture = movieTex4;
                movieTex4.wrapMode = TextureWrapMode.Repeat;
                movieTex4.loop = true;
                movieTex4.Play();
                mDyIndex = 0;
                if (IsInvoking("setDynamicImg")) CancelInvoke("setDynamicImg");
                InvokeRepeating("setDynamicImg", 0, 0.9F);
                //每次按下，IsShock为false,才能保证手柄震动
                if ((int)mTrackedObj.index != -1)
                {
                    IsShock = false;
                    StartCoroutine("Shock", 0.1f);
                }
            }
        }

        void setDynamicImg()
        {
            mDyIndex = (mDyIndex + 1) % 5;
            if (mIndex == 1)
            {
                switch (mDyIndex)
                {
                    case 1:
                        canvasImgDy.sprite = dyImg11;
                        break;
                    case 2:
                        canvasImgDy.sprite = dyImg12;
                        break;
                    case 3:
                        canvasImgDy.sprite = dyImg13;
                        break;
                }
            }
            else if (mIndex == 2)
            {
                switch (mDyIndex)
                {
                    case 1:
                        canvasImgDy.sprite = dyImg21;
                        break;
                    case 2:
                        canvasImgDy.sprite = dyImg22;
                        break;
                    case 3:
                        canvasImgDy.sprite = dyImg23;
                        break;
                }
            }
            else if (mIndex == 3)
            {
                switch (mDyIndex)
                {
                    case 1:
                        canvasImgDy.sprite = dyImg31;
                        break;
                    case 2:
                        canvasImgDy.sprite = dyImg32;
                        break;
                    case 3:
                        canvasImgDy.sprite = dyImg33;
                        break;
                }
            }
            else if (mIndex == 4)
            {
                switch (mDyIndex)
                {
                    case 1:
                        canvasImgDy.sprite = dyImg41;
                        break;
                    case 2:
                        canvasImgDy.sprite = dyImg42;
                        break;
                    case 3:
                        canvasImgDy.sprite = dyImg43;
                        break;
                }
            }

        }

        IEnumerator Shock(float durationTime)
        {            
            //Invoke函数，表示durationTime秒后，执行StopShock函数；
            Invoke("StopShock", durationTime);

            //协程一直使得手柄产生震动，直到布尔型变量IsShock为false;
            while (!IsShock)
            {
                var device = SteamVR_Controller.Input((int)mTrackedObj.index);
                if(device != null)
                {
                    device.TriggerHapticPulse(500);
                }               
                yield return new WaitForEndOfFrame();
            }
        }

        void StopShock()
        {
            IsShock = true; //关闭手柄的震动
        }

        void rotateUI()
        {
            //旋转UI
            if (mRotateUI>0) {
                mRotateUI += 2.0f;
                mUIRoot.transform.Rotate(mUIRoot.transform.up, 2.0f, Space.World);
                if (Mathf.Abs(90.0f - mRotateUI) < 0.1)
                {
                    mRotateUI = 0;                   
                }
            }else if(mRotateUI < 0)
            {
                mRotateUI -= 2.0f;
                mUIRoot.transform.Rotate(mUIRoot.transform.up, -2.0f, Space.World);
                if (Mathf.Abs(90.0f + mRotateUI) < 0.1)
                {
                    mRotateUI = 0;
                }
            }  

        }
    }
}

// IgniteWandCanInter

using UnityEngine;
using System.Collections;
namespace Ignite
{
    public class IgniteWandCanInter : MonoBehaviour
    {

        public bool CanInter()
        {
            return true;
        }
    }
}


// IgniteWandInteract

using UnityEngine;
using System.Collections;
namespace Ignite
{
    public class IgniteWandInteract : MonoBehaviour
    {
        private GameObject mTouchedObject;
        public  Material highMat;
        private Material preMat1, preMat2, preMat3, preMat4;
    
        void Start()
        {
            mTouchedObject = null;
        }

        public GameObject getTouchedObject()
        {
            return mTouchedObject;
        }

        public void setMaterial()
        {
            mTouchedObject.GetComponent<Renderer>().materials[0] = highMat;
        }

        void OnTriggerEnter(Collider collider)
        {
           // Debug.Log("OnTrrigerEnter");
           // Debug.Log(collider.gameObject.name);            
           
            if (collider.gameObject.tag == "prefab1")
            {
                preMat1 = collider.gameObject.GetComponent<Renderer>().material;
                collider.gameObject.GetComponent<Renderer>().material = highMat;
                mTouchedObject = collider.gameObject;
            }
            else if (collider.gameObject.tag == "prefab2")
            {
                preMat2 = collider.gameObject.GetComponent<Renderer>().material;
                collider.gameObject.GetComponent<Renderer>().material = highMat;
                mTouchedObject = collider.gameObject;
            }
            else if (collider.gameObject.tag == "prefab3")
            {
                preMat3 = collider.gameObject.GetComponent<Renderer>().material;
                collider.gameObject.GetComponent<Renderer>().material = highMat;
                mTouchedObject = collider.gameObject;
            }
            else if (collider.gameObject.tag == "prefab4")
            {               
                preMat4 = collider.gameObject.GetComponent<Renderer>().material;
                collider.gameObject.GetComponent<Renderer>().material = highMat;
                mTouchedObject = collider.gameObject;
            }
           
        }
        void OnTriggerExit(Collider collider)
        {
            //Debug.Log("OnTrrigerExit");
           // Debug.Log(collider.gameObject.name);
            if (collider.gameObject.tag == "prefab1" || collider.gameObject.tag == "prefab2"
              || collider.gameObject.tag == "prefab3" || collider.gameObject.tag == "prefab4")
            {
               
                    if (collider.gameObject.tag == "prefab1")
                    {
                        collider.gameObject.GetComponent<Renderer>().material = preMat1;
                    }
                    else if (collider.gameObject.tag == "prefab2")
                    {
                        collider.gameObject.GetComponent<Renderer>().material = preMat2;
                    }
                    else if (collider.gameObject.tag == "prefab3")
                    {
                        collider.gameObject.GetComponent<Renderer>().material = preMat3;
                    }
                    else if (collider.gameObject.tag == "prefab4")
                    {
                        collider.gameObject.GetComponent<Renderer>().material = preMat4;
                    }
                    
                    mTouchedObject = null;
                

             }
        }



    }
}

// RaypickEventArgs

using UnityEngine;
using System.Collections;
using System;
using System.Text;
using System.Security.Cryptography;
using System.IO;

namespace Ignite
{
    public struct RaypickEventArgs
    {
        public uint controllerIndex;
        public uint flags;
        public float distance;
        public Transform target;
    }

    public delegate void RaypickEventHandler(object sender, RaypickEventArgs e);
    public class Raypick : MonoBehaviour
     {   
        public Color color;
        public float thickness = 0.001f;
        public Transform  mCartPos;    //购物车的位置
        public IgniteUI   mIgniteUI;

        private GameObject handler;//手柄模型

        private ArrayList buyList;
        private string buydata;

      
        
        private GameObject holder;
        public GameObject pointer;
        public Shader sihouette;
        private bool isActive = false;
        private bool addRigidBody = false;
        private Transform reference;
        public event RaypickEventHandler PointerIn;
        public event RaypickEventHandler PointerOut;

        Transform previousContact = null;

        private GameObject colliderObject;
        private GameObject grabObject = null;   //抓住的物体
        private GameObject grabObject2 = null;   //抓住的物体
        SteamVR_TrackedObject mTrackedObj;
        public Transform  mJewelryPos; //首饰在手柄上的位置
        private bool      trrigged = false;

        private bool isHighLight = false;
        void Start() 
        {
            colliderObject = null;

            holder = new GameObject();
            holder.transform.parent = this.transform;
            holder.transform.localPosition = Vector3.zero;

            //pointer = GameObject.CreatePrimitive(PrimitiveType.Cube);
            pointer.transform.parent = holder.transform;
            pointer.transform.localScale = new Vector3(thickness, thickness, 100f);
            pointer.transform.localPosition = new Vector3(0f, 0f, 50.001f);
            BoxCollider collider = pointer.GetComponent<BoxCollider>();
            if (addRigidBody)
            {
                if (collider)
                {
                    collider.isTrigger = true;
                }
                Rigidbody rigidBody = pointer.AddComponent<Rigidbody>();
                rigidBody.isKinematic = true;
            }
            else
            {
                if (collider)
                {
                    UnityEngine.Object.Destroy(collider);
                }
            }
            //Material newMaterial = new Material(Shader.Find("Unlit/Color"));
            //newMaterial.SetColor("_Color", color);
            //pointer.GetComponent<MeshRenderer>().material = newMaterial;  
            pointer.GetComponent<MeshRenderer>().material.SetColor("_Color", color);

            mTrackedObj = GetComponent<SteamVR_TrackedObject>();

            handler = null; 
            buyList = new ArrayList();

        }
        
        

        void Update ()
         {
            if (!isActive)
            {
                isActive = true;
                this.transform.GetChild(0).gameObject.SetActive(true);
            }

            float dist = 100f;

            SteamVR_TrackedController controller = GetComponent<SteamVR_TrackedController>();

            if(!trrigged){

            Ray raycast = new Ray(transform.position, transform.forward);
            RaycastHit hit;
            bool bHit = Physics.Raycast(raycast, out hit);

            if (previousContact && previousContact != hit.transform)
            {
                RaypickEventArgs args = new RaypickEventArgs();
                if (controller != null)
                {
                    args.controllerIndex = controller.controllerIndex;
                }
                args.distance = 0f;
                args.flags = 0;
                args.target = previousContact;
                OnPointerOut(args);
                //previousContact = null;
                handlerHighLight(false);
            }

            if (bHit && previousContact != hit.transform)
            {
                RaypickEventArgs argsIn = new RaypickEventArgs();
                if (controller != null)
                {
                    argsIn.controllerIndex = controller.controllerIndex;
                }

               
                previousContact = hit.transform;
              

                if(isJewelry(hit.transform.gameObject) ||hit.transform.gameObject.tag == "btncart" ||hit.transform.gameObject.tag == "btnbuy" )
                {
                    argsIn.distance = hit.distance;
                    argsIn.flags = 0;
                    argsIn.target = hit.transform;
                    colliderObject = hit.transform.gameObject;
                    OnPointerIn(argsIn);
                    handlerHighLight(true);
                }
            }


            if (!bHit)
            {
                previousContact = null;
                colliderObject = null;
            }

            if (bHit && hit.distance < 100f)
            {
                dist = hit.distance;
            }

            if (controller != null && controller.triggerPressed)
            {
                pointer.transform.localScale = new Vector3(thickness * 5f, thickness * 5f, dist);
            }
            else
            {
                pointer.transform.localScale = new Vector3(thickness, thickness, dist);
            }

            pointer.transform.localPosition = new Vector3(0f, 0f, -dist / 2f);
            }

            //抓住物体
            var device = SteamVR_Controller.Input((int)mTrackedObj.index); 
            if(colliderObject !=null && grabObject == null && device.GetTouchDown(SteamVR_Controller.ButtonMask.Trigger))
            {
                //if(colliderObject.tag == "pick")
                //  grabObject = colliderObject;
                //else
                //  grabObject = Instantiate(colliderObject); 

                //grabObject.tag = "pick";

                if (colliderObject.tag == "btncart")
                {
                    addtoCart();                    
                }
                else if (colliderObject.tag == "btnbuy")
                {
                    buy();                    
                }
                else if(isJewelry(colliderObject))
                {                   
                    if(grabObject2 != null)
                    {
                        Destroy(grabObject2);
                    }
                    grabObject = Instantiate(colliderObject); 
                    if(grabObject.tag == "pick1")
                    {
                        mIgniteUI.setJewelry(1);
                    }
                    else if(grabObject.tag == "pick2")
                    {
                        mIgniteUI.setJewelry(2);
                    }
                    else if(grabObject.tag == "pick3")
                    {
                        mIgniteUI.setJewelry(3);
                    }
                    else if(grabObject.tag == "pick4")
                    {
                        mIgniteUI.setJewelry(4);
                    }
                }
            
            }  

            if (grabObject != null && device.GetTouchDown(SteamVR_Controller.ButtonMask.Trigger))
            {
                Vector3 offset = new Vector3(0.0f,0.05f, 0.15f);
                grabObject.transform.SetParent(mJewelryPos);
                grabObject.transform.localPosition = offset;               
                grabObject.transform.localRotation = Quaternion.Euler(-40.0f, 180.0f, 0.0f);   
                grabObject.transform.localScale = new Vector3(2.0f, 2.0f, 2.0f);    

                if(isHighLight)
                {
                    handlerHighLight(false);
                }       
                

                trrigged = true;
                pointer.SetActive(false);

                //mIgniteRayPick.showRay(false);
            }
            else if (grabObject != null && device.GetTouchUp(SteamVR_Controller.ButtonMask.Trigger))
            {
                grabObject.transform.SetParent(null);
                //grabObject.transform.position = mJewelryPos.position;
                grabObject2 = grabObject;
                grabObject = null;
                trrigged = false;
                pointer.SetActive(true);
                //Release = 1;
                //mIgniteRayPick.showRay(true);
            }
        }


        public virtual void OnPointerIn(RaypickEventArgs e)
        {
            if (PointerIn != null)
            {
                PointerIn(this, e);
            }

           
           // handlerHighLight(true);
        }


        public virtual void OnPointerOut(RaypickEventArgs e)
        {
            if (PointerOut != null)
            {
                PointerOut(this, e);
            }
           // handlerHighLight(false);
        }

        bool isJewelry(GameObject obj)
        {
             IgniteWandCanInter r = obj.GetComponent<IgniteWandCanInter>();
            if (r != null)
                return true;
            else
                return false;
        }


        //手柄高亮
        public void handlerHighLight(bool highlight)
        {
            if(handler == null)
                handler = transform.FindChild("Model/body").gameObject; 

            if(highlight)
            {
                isHighLight = true;
                //handler.GetComponent<MeshRenderer> ().materials [0].shader = Shader.Find ("Outlined/Silhouetted Diffuse");
               // handler.GetComponent<MeshRenderer>().material.shader = Shader.Find ("Outlined/Silhouetted Diffuse");
                handler.GetComponent<MeshRenderer>().material.shader = sihouette;
                pointer.GetComponent<MeshRenderer>().material.SetColor("_Color",new Color(1,1,0));
            }
            else
            {
                isHighLight = false;
               // handler.GetComponent<MeshRenderer> ().materials [0].shader = Shader.Find ("Standard");
                handler.GetComponent<MeshRenderer>().material.shader = Shader.Find ("Standard");
                pointer.GetComponent<MeshRenderer>().material.SetColor("_Color", color);
            }
        }

        void addtoCart()
        {
             if (!IsInvoking("JewelryMovetoCart"))
                     InvokeRepeating("JewelryMovetoCart", 0, 0.01F);

        }

        void buy()
        {
            if (buyList.Count == 0) return;
            mIgniteUI.setJewelry(0);
            buyList.Sort();
           
            int buyindex1 = 0, buyindex2 = 0, buyindex3 = 0, buyindex4 = 0;
            foreach (int i in buyList)
            {
                if(i==1) buyindex1++;
                else if(i==2) buyindex2++;
                else if (i == 3) buyindex3++;
                else if (i == 4) buyindex4++;
            }
            buyList.Clear();
            buydata = "{\"detail\":\"";
            if (buyindex1 > 0) buydata += ("28066:" + buyindex1.ToString());
            if (buyindex2 > 0)
            {   if (buyindex1 > 0) buydata += ",";
                buydata += ("39243:" + buyindex2.ToString());
            }
            if (buyindex3 > 0)
            {
                if (buyindex1 > 0 || buyindex2>0) buydata += ",";
                buydata += ("37365:" + buyindex3.ToString());
            }
            if (buyindex4 > 0)
            {
                if (buyindex1 > 0 || buyindex2 > 0 || buyindex3 > 0) buydata += ",";
                buydata += ("39242:" + buyindex4.ToString());
            }
            buydata += "\"}";
            
            
            StartCoroutine(TestPost());

        }

         void JewelryMovetoCart()
        {  
            if(grabObject2)
            {       
                if(grabObject2.tag == "pick1")
                {
                    buyList.Add(1);
                }
                else if(grabObject2.tag == "pick2")
                {
                    buyList.Add(2);
                }
                else if(grabObject2.tag == "pick3")
                {
                    buyList.Add(3);
                }
                else if(grabObject2.tag == "pick4")
                {
                    buyList.Add(4);
                }
                grabObject2.transform.position = Vector3.Lerp(grabObject2.transform.position, mCartPos.position,Time.deltaTime * 1.0f);
                if (Vector3.Distance(grabObject2.transform.position , mCartPos.position)<0.1f)
                {                //mIgniteUI.setJewelry(0);
                    Destroy(grabObject2);
                    CancelInvoke("JewelryMovetoCart");                    
                }
            } 

        }

        //把数据提交到网页
       IEnumerator TestPost()
        {
            //WWW的三个参数: url, postData, headers  
            string url = "http://www.ignjewelry.com/api.php/services/rest";

            WWWForm newForm = new WWWForm();
            newForm.AddField("method", "front.vrcartorder");

            string visa = Convert.ToBase64String(Encoding.Default.GetBytes("vr@ign.vip 123456"));
            visa = "dnJAaWduLnZpcCAxMjM0NTY="; //演示用
            newForm.AddField("visa", visa);

            newForm.AddField("format", "json");

            System.Random rand = new System.Random();
            int vcode = rand.Next(1, 28);
            vcode = 10;//演示用
            newForm.AddField("vcode", vcode.ToString()); //1-28的随机数

            string curlPost = "method=front.vrcartorder&visa=" + visa + "&format=json";
            string pubKey = "O4rDRqwshSBojonvTt4mar21Yv1Ehmqm";
            //string sign = gensign(curlPost, vcode, pubKey);
            string sign = "9e5cf4532551b8be30e3955eef8d9683";//演示用
            newForm.AddField("sign", sign);

            newForm.AddField("debug", "0");

            //string dataArr = "{detail:39242:1,28066:1,37365:1,39243:1}";
            //string dataArr = "{\"detail\":\"28066:1,37365:1,39243:1\"}";

            //Debug.Log(dataArr);
            string dataArr = Convert.ToBase64String(Encoding.Default.GetBytes(buydata));
           // dataArr = "eyJkZXRhaWwiOiIzOTI0MjoxLDI4MDY2OjEsMzczNjU6MSwzOTI0MzoxIn0=";
             
            newForm.AddField("datas", dataArr);


            //发送请求  
            WWW www_instance = new WWW(url, newForm);

            //web服务器返回  
            yield return www_instance;
            if (www_instance.error != null)
            {
                Debug.Log(www_instance.error);
            }
            else
            {
                Debug.Log(www_instance.text);
            }
        }
    }
}